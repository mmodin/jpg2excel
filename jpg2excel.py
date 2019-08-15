import xlsxwriter
import sys
import os
from PIL import Image

def validate_file_size(im):
	pass


def jpg2excel(fp):
	file_name, path = os.path.splitext(os.path.basename(fp))
	im = Image.open(fp)
	w = im.width
	h = im.height
	print(f"Reading {file_name}[{w}x{h}] from disk...")
	hex_colors = ['#%02x%02x%02x' % x for x in im.getdata()]
	
	excel_name = file_name + ".xlsx"
	print(f"Writing data to excel sheet: {excel_name}...")
	workbook = xlsxwriter.Workbook(excel_name)
	worksheet = workbook.add_worksheet()
	index = 0
	for row in range(h):
		for col in range(w):
			cell_format = workbook.add_format()
			cell_format.set_bg_color(hex_colors[index])
			worksheet.write(row, col, ".", cell_format)
			index += 1
	print("Done! Closing file.")
	workbook.close()
	

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Provide the .jpg file name as the only argument!")
		sys.exit()
	jpg2excel(sys.argv[1])
