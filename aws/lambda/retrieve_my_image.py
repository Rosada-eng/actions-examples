import base64
import os

def get_image_path() -> str:
    return os.path.join(os.path.dirname(__file__), "img", "feup.jpg")

def lambda_handler(event, context):
    # Path to the image in the Lambda function deployment package
    image_path = get_image_path()  # Lambda stores the deployed code in /var/task
    
    try:
        # Read the image file and encode it to base64
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')

        # Create the HTML content with the embedded base64 image
        html_content = f"""
        <html>
        <head>
            <title>FEUP - Porto</title>
        </head>
        <body>
            <h1>Faculty logo:</h1>
            <img src="data:image/jpeg;base64,{encoded_image}" alt="FEUP Logo"/>
        </body>
        </html>
        """
        
        # Return the HTML content as the Lambda function response
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': html_content
        }
    
    except Exception as e:
        # Handle the exception if the image cannot be read
        return {
            'statusCode': 500,
            'body': f"Error loading image: {str(e)}"
        }
    
if __name__ == "__main__":
    print(lambda_handler(None, None))