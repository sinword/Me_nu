import base64
import os
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


# Initialize OpenAI chat model
openai_api_key = os.getenv(
    'OPENAI_API_KEY', 'sk-proj-SR7afOu2h9tuPYXA9FEWT3BlbkFJrkTm9JGQjRRWlcQDcYpy')
chat = ChatOpenAI(model_name="gpt-4o", temperature=0.2, openai_api_key=openai_api_key)

# Path to your image
# List of image paths
# IMAGE_PATHS = [
#     r'/Users/hsinyi/Downloads/menu10_1.jpg',
#     r'/Users/hsinyi/Downloads/menu10_2.jpg'
# ]

IMAGE_PATHS = [r'/Users/hsinyi/Downloads/menu13.jpg']

# Function to encode image as base64 string
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

# Construct base messages
base_messages = [
    SystemMessage(content="你是一個能擷取菜單內容的助手。請保留菜單的原始項目名稱和價格，不做任何更改。請確保提取的內容準確且格式清晰。")
]

# Process each image
for image_path in IMAGE_PATHS:
    # Encode the image
    base64_image = encode_image(image_path)

    # Construct human message with the encoded image
    human_message = HumanMessage(
        content=[
            {"type": "text", "text": "這是菜單圖片"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{base64_image}", "detail": "high"}}
        ]
    )

    # Combine system and human messages
    messages = base_messages + [human_message]

    # Send messages to OpenAI and get response
    response = chat(messages)

    # Display or process the response for each image
    print(f"Response for {image_path}:")
    print(response.content)
    print("\n")

# After processing all images
print("Finished processing all images.")