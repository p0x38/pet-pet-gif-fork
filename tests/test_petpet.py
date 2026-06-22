import os
from pathlib import Path
from petpetgif import petpet

def test_make_gif(tmp_path):
	from PIL import Image
	dummy_input = tmp_path / "input.png"
	Image.new("RGBA", (10, 10), "red").save(dummy_input)

	output_gif = tmp_path / "output.gif"

	petpet.make(dummy_input, output_gif)

	assert output_gif.exists()
	assert output_gif.stat().st_size > 0
