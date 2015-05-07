%----------------------------------------------------------------------------------------
%	CLASS OPTIONS AND REQUIRED PACKAGES
%----------------------------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass{article}

\usepackage[hmargin=1cm, vmargin=0.75cm]{geometry} % Specifies horizontal and vertical page margins
\usepackage{wasysym}
\usepackage{pdfcomment}  % For the interactive comments
\usepackage{hyperref}    % Required for links

% Set parameters of Hyperlinks
\hypersetup{hidelinks}

%----------------------------------------------------------------------------------------
%	COLORS
%----------------------------------------------------------------------------------------

\usepackage[usenames,dvipsnames]{xcolor} % Required for custom colors

\definecolor{primary}{HTML}{2b2b2b} % The primary document color for content text
\definecolor{headings}{HTML}{6A6A6A} % The color of the large sections
\definecolor{headtitle}{HTML}{4899DD} % The color of the main sections
\definecolor{mainhead}{HTML}{6A77BB} % The color of the main sections
\definecolor{bullets}{HTML}{6AAA6A} % The color of the main sections
\definecolor{bullets2}{HTML}{4899DD} % The color of the main sections
\definecolor{subheadings}{HTML}{333333} % The color of subsections and places worked/studied
\definecolor{date}{HTML}{666666} % The color used for the Last Updated text at the top right
\definecolor{lightgray}{HTML}{CCCCCC} % The primary document color for content text
\definecolor{lightblue}{HTML}{4899DD} % The color of the main sections
\definecolor{white}{HTML}{FFFFFF} % The color of the main sections
\definecolor{tweetblue}{HTML}{598DCA} % The color of the Twitter logo
\definecolor{wordgray}{HTML}{464646} % The color of the gray Wordpress logo

%----------------------------------------------------------------------------------------
%	FONTS
%----------------------------------------------------------------------------------------

\usepackage{fontspec} % Required for specifying custom fonts in XeLaTeX

\setmainfont[Color=primary, Path = fonts/lato/,BoldItalicFont=Lato-RegIta,BoldFont=Lato-Reg,ItalicFont=Lato-LigIta]{Lato-Lig} % The primary font for content text; defines bold, italic and bold-italic as well

\setsansfont[Scale=MatchLowercase,Mapping=tex-text, Path = fonts/raleway/]{Raleway-ExtraLight} % The font used where \sfffamily is called

%----------------------------------------------------------------------------------------
%	MAIN HEADING COMMAND
%----------------------------------------------------------------------------------------

\newcommand{\namesection}[3]{ % Defines the command for the main heading
	\centering{ % Center the name
		\fontsize{40pt}{60pt} % Font size
		\fontspec[Path = fonts/lato/]{Lato-Hai}\selectfont #1 % First name font
		\fontspec[Path = fonts/lato/]{Lato-Lig}\selectfont #2 % Last name font
	} \\[5pt] % Whitespace between the name and contact information
	\centering{ % Center the contact information
		\color{headings} % Use the headings color
		\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{14pt}\selectfont #3 % Contact font
	}
	\noindent\makebox[\linewidth]{\color{headings}\rule{\paperwidth}{0.4pt}} % Horizontal rule
	\vspace{-5pt} % Reduce whitespace after the rule slightly
}

%----------------------------------------------------------------------------------------
%	SECTION TITLE STYLING AND SPACING
%----------------------------------------------------------------------------------------

\usepackage{titlesec} % Required for customizing section/subsection/etc titles

\titlespacing{\section}{0pt}{0pt}{0pt} % Removes the spacing around the main section titles
\titlespacing{\subsection}{0pt}{0pt}{0pt} % Removes the spacing around the subsections
\newcommand{\sectionspace}{\vspace{8pt}} % Defines a command to add a set amount of space after sections and subsections

\titleformat{\section}{ % Customize the large section titles
\color{mainhead}\scshape\fontspec[Path = fonts/lato/]{Lato-Lig}\fontsize{16pt}{24pt}\selectfont \raggedright\bfseries\uppercase}{}{0em}{}

\titleformat{\subsection}{ % Customize the subsections and places worked/studied titles
\color{subheadings}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{12pt}{12pt}\selectfont\bfseries\uppercase}{}{0em}{}

\newcommand{\runsubsection}[1]{ % Used for creating subsections where a description is required on the same line
\color{subheadings}\fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{12pt}{12pt}\selectfont\bfseries\uppercase {#1} \normalfont}

\newcommand{\descript}[1]{ % Used for describing the subsection either on the same line or underneath
\color{subheadings}\raggedright\scshape\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont {#1 \\} \normalfont}

\newcommand{\location}[1]{ % Used for specifying a duration and/or location under a subsection
\color{headings}\raggedright\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{10pt}{12pt}\selectfont {#1\\} \normalfont}

%----------------------------------------------------------------------------------------
%	COLUMN STYLING AND SPACING
%----------------------------------------------------------------------------------------

\usepackage{array} % Required to customize the dimensions in tabular spaces
\newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\usepackage{amssymb}

%----------------------------------------------------------------------------------------
%	SECTION TITLE STYLING AND SPACING
%----------------------------------------------------------------------------------------

\newenvironment{tightitemize} % Defines the tightitemize environment which modifies the itemize environment to be more compact
{	\vspace{-\topsep}
	\begin{itemize}
		\itemsep 1pt
		\parskip 0pt
		\parsep 0pt}
{	\end{itemize}
	\vspace{-\topsep}}

%----------------------------------------------------------------------------------------
%	STYLE FOR CHARTS
%----------------------------------------------------------------------------------------

\usepackage{tikz}        % For cool graphs
\def\angle{90}
\def\radius{1}
\def\inradius{0.65}
\def\iconwidth{20pt}