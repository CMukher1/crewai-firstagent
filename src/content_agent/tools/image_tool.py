import os
import requests
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from dotenv import load_dotenv

class ImageSearchInput(BaseModel):
    """Input for ImageSearchTool."""
    query: str = Field(..., description="Search query for finding images")
    num_images: int = Field(default=3, description="Number of images to download")

class ImageSearchTool(BaseTool):
    name: str = "Image Search and Download Tool"
    description: str = """
    Downloads images related to a topic. Just provide the search query as a simple string.
    Example: 'ICC Champions Trophy 2025 stadium' or 'Cricket World Cup trophy'
    """
    args_schema: Type[BaseModel] = ImageSearchInput

    def _run(self, query: str, num_images: int = 3) -> str:
        load_dotenv()
        
        # Get the absolute path to the assets directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        assets_dir = os.path.join(base_dir, 'assets')
        os.makedirs(assets_dir, exist_ok=True)

        print(f"Searching for images with query: {query}")
        print(f"Saving to directory: {assets_dir}")

        try:
            # Use SerperDev to search for images
            response = requests.post(
                "https://api.serper.dev/images",
                headers={
                    "X-API-KEY": os.getenv("SERPER_API_KEY"),
                    "Content-Type": "application/json"
                },
                json={"q": query, "gl": "us", "num": num_images}
            )
            
            if response.status_code != 200:
                print(f"Error from Serper API: {response.text}")
                return f"Error from Serper API: {response.text}"

            images = response.json().get('images', [])
            if not images:
                print("No images found in the response")
                return "No images found for the query"

            downloaded_images = []
            for i, image in enumerate(images[:num_images]):
                try:
                    image_url = image.get('imageUrl')
                    if not image_url:
                        print(f"No image URL for image {i+1}")
                        continue

                    print(f"Downloading image from: {image_url}")
                    img_response = requests.get(image_url, timeout=10)
                    
                    if img_response.status_code == 200:
                        # Create filename based on query
                        filename = f"{query.replace(' ', '_')}_{i+1}.jpg"
                        filepath = os.path.join(assets_dir, filename)
                        
                        # Save image
                        with open(filepath, 'wb') as f:
                            f.write(img_response.content)
                        downloaded_images.append(filename)
                        print(f"Successfully saved image to: {filepath}")

                except Exception as e:
                    print(f"Error downloading image {i+1}: {str(e)}")
                    continue

            if downloaded_images:
                success_msg = f"Successfully downloaded {len(downloaded_images)} images: {', '.join(downloaded_images)}"
                print(success_msg)
                return success_msg
            
            return "Failed to download any images."

        except Exception as e:
            error_msg = f"Error searching for images: {str(e)}"
            print(error_msg)
            return error_msg 