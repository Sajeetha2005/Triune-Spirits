import cv2
import numpy as np
img = cv2.imread(r"C:\Users\sajur\OneDrive\Pictures\133896006134752582.jpg")
if img is None:
    print("❌ Error: Image not found. Check the path!")
    exit()
orig = img.copy()
ratio = img.shape[0] / 500.0
img = cv2.resize(img, (600, int(img.shape[0] * 600 / img.shape[1])))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray, 75, 200)
cv2.imshow("Edges", edges) 
cv2.waitKey(0)
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
doc_cnt = None
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)  
    if len(approx) == 4:
        doc_cnt = approx
        break
if doc_cnt is None:
    print("⚠ No 4-corner contour found, using bounding box instead.")
    c = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)
    doc_cnt = np.array([[x, y], [x+w, y], [x+w, y+h], [x, y+h]])
def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

doc_cnt = order_points(doc_cnt.reshape(4, 2) * ratio)
(tl, tr, br, bl) = doc_cnt
widthA = np.linalg.norm(br - bl)
widthB = np.linalg.norm(tr - tl)
maxWidth = max(int(widthA), int(widthB))

heightA = np.linalg.norm(tr - br)
heightB = np.linalg.norm(tl - bl)
maxHeight = max(int(heightA), int(heightB))

dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]
], dtype="float32")

M = cv2.getPerspectiveTransform(doc_cnt, dst)
warp = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))
warp_gray = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
warp_bin = cv2.adaptiveThreshold(
    warp_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)
output = np.hstack((cv2.resize(orig, (600, 800)), cv2.resize(warp_bin, (600, 800))))
cv2.imshow("Original vs Scanned", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
