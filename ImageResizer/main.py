import cv2

def resize_image(input_path,output_path,new_width,new_height):

    original_image = cv2.imread(input_path)
    resized_image = cv2.resize(original_image, (new_width, new_height))
    cv2.imwrite(output_path, resized_image)

if __name__ == "__main__":
        input_image_path = input('Enter input image path: ') 
        output_image_path = input('Enter output image path: ')

        new_width = input('Enter Width: ')
        new_height = input('Enter Height: ')

        resize_image(input_image_path, output_image_path, new_width, new_height)

        print("Image resized successfully!")