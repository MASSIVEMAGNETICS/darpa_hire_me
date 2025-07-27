from bando_super_fractal_language_model.model import BandoSuperFractalLanguageModel

def main():
    """Main function to run the Bando Super Fractal Language Model."""
    model = BandoSuperFractalLanguageModel()
    input_data = "This is a test input."
    output = model.process(input_data)
    print(f"Input: {input_data}")
    print(f"Output: {output}")

if __name__ == "__main__":
    main()
