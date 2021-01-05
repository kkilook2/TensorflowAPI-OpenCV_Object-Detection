import cv2
import numpy as np

src1 = np.array([[3,2], [2,2]], dtype=np.double)
src2 = np.array([13,10], dtype=np.double)

dst = cv2.solve(src1, src2, flags= cv2.DECOMP_LU)
print(dst)