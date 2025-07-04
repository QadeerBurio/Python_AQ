import numpy as np
import cv2


def harmonic_mean_filter(image, kernel_size):
    # Get the dimensions of the image
    rows, cols = image.shape

    # Create an empty array to store the output
    filtered_image = np.zeros((rows, cols), dtype=np.float32)

    # Define the padding for the image based on the kernel size
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='constant', constant_values=0)

    # Apply the harmonic mean filter
    for i in range(pad_size, rows + pad_size):
        for j in range(pad_size, cols + pad_size):
            # Get the kernel window around the pixel
            window = padded_image[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1]

            # Calculate the harmonic mean of the window
            harmonic_mean = np.sum(1.0 / (window + 1e-6))  # Add small epsilon to avoid division by zero
            filtered_image[i - pad_size, j - pad_size] = (kernel_size * kernel_size) / harmonic_mean

    # Convert the result back to 8-bit image format
    filtered_image = np.clip(filtered_image, 0, 255)
    filtered_image = filtered_image.astype(np.uint8)

    return filtered_image


# Load the image in grayscale
image = cv2.imread('', cv2.IMREAD_GRAYSCALE)

# Apply the harmonic mean filter with a kernel size of 3x3
kernel_size = 3
filtered_image = harmonic_mean_filter(image, kernel_size)

# Save and display the result
cv2.imwrite('filtered_image.jpg', filtered_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
