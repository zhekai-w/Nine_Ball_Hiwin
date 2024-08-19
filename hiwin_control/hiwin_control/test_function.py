# import cv2
# import numpy as np

# def adjust_temperature(image, temperature):
#     # Convert the image to the LAB color space
#     lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

#     # Split the LAB image into L, A, and B channels
#     l, a, b = cv2.split(lab)

#     # Apply the temperature adjustment to the A and B channels
#     a = np.clip(a + temperature, 0, 255).astype(np.uint8)
#     b = np.clip(b + temperature, 0, 255).astype(np.uint8)

#     # Merge the channels back together
#     adjusted_lab = cv2.merge((l, a, b))

#     # Convert back to BGR color space
#     adjusted = cv2.cvtColor(adjusted_lab, cv2.COLOR_LAB2BGR)

#     return adjusted

# def adjust_contrast(image, contrast_factor):
#     # Create a blank array with the same shape as the input image
#     blank = np.zeros(image.shape, image.dtype)

#     # Adjust the contrast using cv2.addWeighted()
#     adjusted = cv2.addWeighted(image, contrast_factor, blank, 1-contrast_factor, 0)

#     return adjusted


# def add_shadow(image, shadow_offset=(20, 20), shadow_blur=5, shadow_opacity=0.5):
#     # Create a blank image with the same dimensions as the input
#     shadow = np.zeros(image.shape[:2], dtype=np.uint8)

#     # Create a white rectangle on the blank image
#     shadow[shadow_offset[1]:, shadow_offset[0]:] = 255

#     # Blur the shadow
#     shadow = cv2.GaussianBlur(shadow, (shadow_blur*2+1, shadow_blur*2+1), 0)

#     # Invert the shadow and adjust opacity
#     shadow = 255 - shadow
#     shadow = cv2.merge([shadow, shadow, shadow])
#     shadow = (shadow * shadow_opacity).astype(np.uint8)

#     # Combine the original image with the shadow
#     result = cv2.add(image, shadow)

#     return result

# # Load an image
# image = cv2.imread('Screenshot from 2024-05-23 00-42-32.png')

# # Adjust temperature (positive values for warmer, negative for cooler)
# warm_image = adjust_temperature(image, 10)  # Warmer
# cool_image = adjust_temperature(image, -30)  # Cooler
# contrast_image = adjust_contrast(image, 1.5)
# shadow_image = add_shadow(image)

# # Save the results
# cv2.imwrite('warm_image.jpg', warm_image)
# cv2.imwrite('cool_image.jpg', cool_image)
# cv2.imwrite('contrast_image.jpg', contrast_image)
# cv2.imwrite('shadow_image.jpg', shadow_image)


list = ['aaa', 'bbb', 'ccc']

if 'aaa' in list:
    pass
else:
    print('hahahaha')

print('aaa in list')
