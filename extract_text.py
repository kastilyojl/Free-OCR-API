import requests #pip install requests
import json

def ocr_space_file(filename, overlay=False, api_key='your_api_key', language='eng', OCREngine=2):
    """OCR.space API request with local file."""
    payload = {
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language,
        'OCREngine': OCREngine,
    }
    with open(filename, 'rb') as f:
        print("Sending request to OCR API...")
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          timeout=10)

    if r.status_code != 200:
        print(f"Error: {r.status_code} - {r.text}")
        return None

    return r.content.decode()

if __name__ == "__main__":

    response = ocr_space_file(filename=r"lorem-ipsum.jpg",
                              language='eng',
                              OCREngine=2)

    if response:
        print("Response:", response)

        try:
            json_response = json.loads(response)
            parsed_results = json_response.get("ParsedResults", [])

            if parsed_results:
                extracted_text = parsed_results[0].get("ParsedText", "")
                print("\nExtracted Text:\n\n", extracted_text) # Display the extracted text in console

            else:
                print("No text found.")
        except json.JSONDecodeError as e:
            print("Error parsing JSON response:", e)
