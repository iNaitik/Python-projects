# gesture_to_adb.py
# pip install mediapipe opencv-python
import os
import shutil
import cv2, time, subprocess
import mediapipe as mp
from collections import deque

# ---- params ----
BUFFER_LEN = 12
# horizontal params
D_THRESH = 0.18     # fraction of camera width to count as horizontal swipe
Y_MAX = 0.20        # allowed vertical drift when detecting horizontal swipe
V_MIN = 0.4         # min horizontal velocity (units/sec)
V_MAX = 8.0
# vertical params
U_THRESH = 0.18     # fraction of camera height to count as vertical swipe
X_MAX = 0.20        # allowed horizontal drift when detecting vertical swipe
VY_MIN = 0.35       # min vertical velocity (units/sec)
VY_MAX = 8.0
COOLDOWN = 0.6      # seconds between accepted gestures
SWIPE_PIXEL_DISTANCE = 600  # fallback pixel distance for adb swipe if computed coords not used

# Require this many fingers to be extended at gesture start
REQUIRED_FINGERS = 2

# Try to locate adb automatically
ADB_CMD = shutil.which("adb")
if ADB_CMD is None:
    # If not in PATH, set full path to adb.exe here:
    ADB_FULL_PATH = r"C:\Users\Naitik\Downloads\platform-tools-latest-windows\platform-tools\adb.exe"  # <-- CHANGE THIS to your adb.exe path if different
    if os.path.exists(ADB_FULL_PATH):
        ADB_CMD = ADB_FULL_PATH
    else:
        raise FileNotFoundError(
            "adb not found. Either add adb to PATH or set ADB_FULL_PATH variable in the script "
            "to point to your adb.exe"
        )

def adb_shell(cmd):
    full_cmd = [ADB_CMD, "shell"] + cmd.split()
    p = subprocess.run(full_cmd, capture_output=True, text=True)
    return p.stdout, p.stderr

def get_screen_size():
    out, err = adb_shell("wm size")
    try:
        parts = out.strip().split()[-1].split('x')
        return int(parts[0]), int(parts[1])
    except:
        return None

def adb_swipe_pixels(x1,y1,x2,y2,duration_ms=200):
    adb_shell(f"input swipe {int(x1)} {int(y1)} {int(x2)} {int(y2)} {int(duration_ms)}")

# ---- mediapipe ----
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
# buffer will store tuples: (x_norm, y_norm, t, extended_finger_count_at_sample)
buffer = deque(maxlen=BUFFER_LEN)
cooldown_until = 0
screen_size = get_screen_size()
print("Android screen size:", screen_size)

def count_extended_index_middle(landmarks):
    """
    Simple heuristic: count index and middle finger as 'extended' if fingertip.y < pip.y
    (works when palm faces camera roughly upright). Uses landmarks indices:
      index tip = 8, index pip = 6
      middle tip = 12, middle pip = 10
    Returns number of extended fingers (0..2).
    """
    try:
        idx_extended = 1 if landmarks.landmark[8].y < landmarks.landmark[6].y else 0
        mid_extended = 1 if landmarks.landmark[12].y < landmarks.landmark[10].y else 0
        return idx_extended + mid_extended
    except:
        return 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    h, w = frame.shape[:2]
    t = time.time()
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0]
        x_norm = lm.landmark[8].x
        y_norm = lm.landmark[8].y
        # count extended fingers (index + middle) at this sample
        extended_cnt = count_extended_index_middle(lm)
        buffer.append((x_norm, y_norm, t, extended_cnt))

        cx, cy = int(x_norm * w), int(y_norm * h)
        cv2.circle(frame, (cx, cy), 8, (0,255,0), -1)
        # show extended finger count on frame
        cv2.putText(frame, f"Fingers:{extended_cnt}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,200,255), 2)

        if len(buffer) >= 6 and t > cooldown_until:
            x_old, y_old, t_old, ext_old = buffer[0]
            x_new, y_new, t_new, ext_new = buffer[-1]
            dx = x_new - x_old
            dy = y_new - y_old
            dt = max(1e-6, t_new - t_old)
            vx = dx / dt
            vy = dy / dt

            # require the gesture to have started with enough fingers extended
            if ext_old < REQUIRED_FINGERS:
                # not started with required fingers; skip evaluation
                pass
            else:
                # PRIORITIZE vertical gestures if vertical displacement significant
                # UP (normalized y increases downward, so negative dy is upward movement)
                if (-dy) >= U_THRESH and abs(dx) <= X_MAX and (-vy) >= VY_MIN and (-vy) <= VY_MAX:
                    print("DETECTED SWIPE UP")
                    cooldown_until = t + COOLDOWN
                    if screen_size:
                        sw, sh = screen_size
                        x1 = int(sw * 0.5); y1 = int(sh * 0.75)
                        x2 = int(sw * 0.5); y2 = int(sh * 0.25)
                        adb_swipe_pixels(x1,y1,x2,y2)
                    else:
                        adb_swipe_pixels(500, 1200, 500, 400)
                    buffer.clear()

                # DOWN
                elif dy >= U_THRESH and abs(dx) <= X_MAX and vy >= VY_MIN and vy <= VY_MAX:
                    print("DETECTED SWIPE DOWN")
                    cooldown_until = t + COOLDOWN
                    if screen_size:
                        sw, sh = screen_size
                        x1 = int(sw * 0.5); y1 = int(sh * 0.25)
                        x2 = int(sw * 0.5); y2 = int(sh * 0.75)
                        adb_swipe_pixels(x1,y1,x2,y2)
                    else:
                        adb_swipe_pixels(500, 400, 500, 1200)
                    buffer.clear()

                # HORIZONTAL gestures: NOTE: inverted mapping per your request
                # If hand moves LEFT (dx < -D_THRESH) -> trigger PHONE SWIPE RIGHT
                if dx <= -D_THRESH and abs(dy) <= Y_MAX and vx <= -V_MIN and vx >= -V_MAX:
                    print("DETECTED HAND MOVE LEFT -> PHONE SWIPE RIGHT")
                    cooldown_until = t + COOLDOWN
                    if screen_size:
                        sw, sh = screen_size
                        # phone swipe right (left->right)
                        x1 = int(sw * 0.25); y1 = int(sh * 0.5)
                        x2 = int(sw * 0.75); y2 = int(sh * 0.5)
                        adb_swipe_pixels(x1,y1,x2,y2)
                    else:
                        adb_swipe_pixels(100, 500, 700, 500)
                    buffer.clear()

                # If hand moves RIGHT (dx > D_THRESH) -> trigger PHONE SWIPE LEFT
                elif dx >= D_THRESH and abs(dy) <= Y_MAX and vx >= V_MIN and vx <= V_MAX:
                    print("DETECTED HAND MOVE RIGHT -> PHONE SWIPE LEFT")
                    cooldown_until = t + COOLDOWN
                    if screen_size:
                        sw, sh = screen_size
                        # phone swipe left (right->left)
                        x1 = int(sw * 0.75); y1 = int(sh * 0.5)
                        x2 = int(sw * 0.25); y2 = int(sh * 0.5)
                        adb_swipe_pixels(x1,y1,x2,y2)
                    else:
                        adb_swipe_pixels(700, 500, 100, 500)
                    buffer.clear()

    else:
        if buffer and time.time() - buffer[-1][2] > 0.4:
            buffer.clear()

    # show debug numbers (optional)
    # cv2.putText(frame, f"dx:{dx:.2f} dy:{dy:.2f}", (10,h-20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

    cv2.imshow("gesture", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
