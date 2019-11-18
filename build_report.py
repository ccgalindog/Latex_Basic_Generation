from glob import glob

def build_header( final_text, title_doc, date_doc, logo_path ):
	final_text.write('\documentclass{article}\n')
	final_text.write('\\usepackage[utf8]{inputenc}\n')
	final_text.write('\\usepackage{graphicx}\n')
	final_text.write('\\usepackage[utf8]{inputenc}\n')
	final_text.write('\\usepackage[graphicx]{realboxes}\n')
	final_text.write('\\usepackage{longtable}\n')
	final_text.write('\\usepackage{array}\n')
	final_text.write('\\newcolumntype{H}{>{\setbox0=\hbox\bgroup}c<{\egroup}@{}}\n')
	final_text.write('\\usepackage{float}\n')
	final_text.write('\\usepackage{booktabs} \n \n \n \n')

	final_text.write('\\title{' + '{}'.format( title_doc ) + '}\n')
	final_text.write('\\author{ ----- }\n')
	final_text.write('\\date{' + '{}'.format( date_doc ) + '}\n')
	final_text.write('\\begin{document}\n')
	final_text.write('\\begin{figure}\n')
	final_text.write('\centering\n')
	final_text.write('\includegraphics[scale=0.2]{' + '{}'.format(logo_path) + '}\n' )
	final_text.write('\end{figure}\n')
	final_text.write('\maketitle\n')
	final_text.write('\n \n \n')
	final_text.write('\section{Introduction}\n')
	final_text.write('***Write here*** \n \n \n ')


	return final_text



def print_graphics( final_text, figure_caption, each_picture_path ):
	final_text.write( "\\begin{figure}[h]\n")
	final_text.write( "\includegraphics[width=1.0\linewidth]{" + "{}".format(each_picture_path) + "}\n" )
	final_text.write( "\caption{" + "{}".format( figure_caption ) + "}\n" )
	final_text.write( "\centering\n" )
	final_text.write( "\end{figure}\n" )
	return final_text

def print_table( final_text, table_caption, each_table_path ):
	final_text.write('\\begin{table}[]\n' )
	final_text.write('\centering\n')
	final_text.write('\caption{' + '{}'.format(table_caption) + '}\n')
	table_lines = [ someline.rstrip('\n') for someline in open( each_table_path, 'r' ) ]

	for any_line in table_lines:
		if 'egin{tabular}{' in any_line:
			code_is = any_line.split('}{')
			any_line = '\\begin{tabular}{'+'H|'+'c|'*( len(code_is[1][:-1]) ) + '}'
		final_text.write( any_line + '\n')
	final_text.write('\end{table}\n')
	return final_text


def build_latex_report( report_title, report_date, logo_path, outdocument_path, pictures_folder, dic_capt_figures, tables_folder, dic_capt_tables, keyname_order ):
	'''	
	report_title: document title
	report_date: date for the document
	logo_path: path to a cover image
	outdocument_path: path to output tex file to be created
	pictures_folder: path to folder where images are located. Format needed on figures:  fig_{num}_{keyname}_
	tables_folder: path to folder where tables are located. Format needed on tables: tab_{num}_{keyname}_.txt
	dic_capt_figures: dictionary with the form: { 'keyname of the fig' : 'Caption string for the fig'} 
	dic_capt_tables: dictionary with the form: { 'keyname of the tab' : 'Caption string for the tab'} 
	keyname_order: list of keynames of every element to put in the document in order
	'''
	final_text = open( outdocument_path, 'w' )
	final_text = build_header( final_text, report_title, report_date, logo_path )
	all_pictures = glob( pictures_folder+'/*' )
	all_tables = glob( tables_folder+'/*' )


	for eachkey in keyname_order:
		if (eachkey[:3] == 'fig'):	
			figure_caption = dic_capt_figures[eachkey]
			ijk = 0
			found_path = 0
			while (ijk < len(all_pictures)) and (found_path == 0):
				each_picture_path = all_pictures[ijk]
				if eachkey in each_picture_path:
					found_path = 1
				ijk = ijk + 1
			final_text = print_graphics( final_text, figure_caption, each_picture_path )

		elif (eachkey[:3] == 'tab'):	
			table_caption = dic_capt_tables[eachkey]
			ijk = 0
			found_path = 0
			while (ijk < len(all_tables)) and (found_path == 0):
				each_table_path = all_tables[ijk]
				if eachkey in each_table_path:
					found_path = 1
				ijk = ijk + 1
			final_text = print_table( final_text, table_caption, each_table_path )
		final_text.write('\n \n \n \n')
		

	final_text.write('\end{document}')
	final_text.close()

		
	

if __name__ == '__main__':
	main()