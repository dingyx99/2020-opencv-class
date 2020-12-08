import numpy as np

def BGR2GRAY(img:np.array):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()

    out = 0.2126*r+0.7152*g+0.0722*b
    out = out.astype(np.uint8)

    return out

def otsu_binarization(img:np.array, th:int = 128):
    H, W = img.shape
    out = img.copy()

    max_sigma = 0
    max_t = 0

    for _t in range(1, 255):
        v0 = out[np.where(out < _t)]
        m0 = np.mean(v0) if len(v0) > 0 else 0.
        w0 = len(v0) / (H * W)
        v1 = out[np.where(out >= _t)]
        m1 = np.mean(v1) if len(v1) > 0 else 0.
        w1 = len(v1) / (H * W)
        sigma = w0 * w1 *((m0 - m1) ** 2)
        if sigma > max_sigma:
            max_sigma = sigma
            max_t = _t
    
    print("Thresold >>", max_t)
    th = max_t
    out[out < th] = 0
    out[out >= th] = 255
    return out

def Dilate(img:np.array, Dil_time:int = 1):
    H, W = img.shape
    MF = np.array(((0, 1, 0),
                    (1, 0, 1),
                    (0, 1, 0)), np.int)
    
    out = img.copy()
    for i in range(Dil_time):
        tmp = np.pad(out, (1, 1), 'edge')
        for y in range(1, H):
            for x in range(1, W):
                if np.sum(MF * tmp[y-1:y+2, x-1:x+2]) >= 255:
                    out[y, x] = 255
    
    return out

def Erode(img:np.array, Erode_time:int=1):
    H, W = img.shape
    out = img.copy()

    MF = np.array(((0, 1, 0),
                    (1, 0, 1),
                    (0, 1, 0)), np.int)
    
    for i in range(Erode_time):
        tmp = np.pad(out, (1, 1), 'edge')
        for y in range(1, H):
            for x in range(1, W):
                if(np.sum(MF * tmp[y-1:y+2, x-1:x+2])) < 255 * 4:
                    out[y, x] = 0
    
    return out

def Closing(img:np.array, time:int = 1):
    out = Dilate(img ,time)
    out = Erode(out, time)

    return out

def Opening(img:np.array, time:int = 1):
    out = Erode(img, time)
    out = Dilate(out, time)

    return out