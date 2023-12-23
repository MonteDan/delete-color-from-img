from PIL import Image

def remove_color(input_image_path, output_image_path, target_color, tolerance=30):

  image = Image.open(input_image_path)

  if image.mode not in ('RGB', 'RGBA'):
    image = image.convert('RGBA')
  
  image_data = list(image.getdata())

  lower_bound = [max(c - tolerance, 0) for c in target_color]
  upper_bound = [min(c + tolerance, 255) for c in target_color]

  modified_data = [
    (0, 0, 0, 0) if all(lower <= value <= upper for lower, value, upper in zip(lower_bound, pixel, upper_bound))
    else pixel
    for pixel in image_data
  ]

  result_image = Image.new("RGBA", image.size)
  result_image.putdata(modified_data)
  result_image.save(output_image_path)


'''
/**

  * ? Example use

  input_image_path = "input_image.jpg"
  output_image_path = "output_image.png"
  target_color = [255, 0, 0] 
  tolerance = 30  

  remove_color(input_image_path, output_image_path, target_color, tolerance)

*/
'''




