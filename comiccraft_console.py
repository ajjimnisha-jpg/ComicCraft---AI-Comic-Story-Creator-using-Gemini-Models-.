from google import genai

API_KEY = "YOUR_GEMINI_API_KEY"
client = genai.Client(api_key=API_KEY)

def main():
    print("=" * 55)
    print("COMICCRAFT - AI COMIC STORY CREATOR")
    print("=" * 55)

    idea = input("Enter your comic idea: ").strip()
    panels = int(input("Enter number of panels (2-10): "))

    prompt = f"""Create a comic story about: {idea}
Create exactly {panels} panels.
For each panel provide Scene, Characters, Dialogue and Narration.
Also provide a title and character descriptions.
Use simple English."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\n" + response.text)

if __name__ == "__main__":
    main()
