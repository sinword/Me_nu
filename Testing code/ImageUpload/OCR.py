import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

os.environ['TESSDATA_PREFIX'] = '/usr/local/share/'

# Path to your image
image_path = r'/Users/hsinyi/Downloads/menu.jpg'

# Load the image
image = Image.open(image_path)

image.show()

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image, lang="chi_tra")

print("Extracted text: ")
print(text)

# # You can then pass this extracted text to the OpenAI model for further processing
# messages = [
#     SystemMessage(content="你是一個有用的、能整理中文菜單內容的助手。請幫我將以下的中文文字整理成合理的菜單內容，並保留原始菜品名稱。"),
#     HumanMessage(content=text)
# ]

# # Send messages to OpenAI and get response
# response = chat(messages)

# # Display or process the response
# print(response.content)
