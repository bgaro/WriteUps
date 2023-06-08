import cv2


def main():
    image_to_load = "marguerite.png"
    image = cv2.imread(image_to_load)
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            for k in range(0, image.shape[2]):
                image[i][j][k] = (image[i][j][k] & 1) * 255

    cv2.imwrite("lsb.png", image)


if __name__ == "__main__":
    main()
