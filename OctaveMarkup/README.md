# GNU Octave Markup

This project intends to create Markup support for GNU Octave, based on the [Markup](http://de.mathworks.com/help/matlab/matlab_prog/marking-up-matlab-comments-for-publishing.html "MATLAB - Publishing Markup") defined by MATLAB, so that both methods are compatible.

This **Octave Markup** should:
- Be compatible with [MATLAB Markup for Publishing Code](http://de.mathworks.com/help/matlab/matlab_prog/publishing-matlab-code.html "Publishing MATLAB Code").
- Identify Markup and Help text as separated
- Parse into PDF, LaTeX and HTML formats.
- Allow the customization of documentation styles.
- Be light and (perhaps) portable.
- Be also compatible with the format of the help options of each file.

In the same sense, the **Octave Markup** could:
- Have both interactions directly through the Command Line or with an interactive fashion within Octave's GUI.
- Be able to generate further outputs like XHTML, ePub, RTF, Man pages, Qt Help, ODF, etc.

This project is from now under constant development.

References
----------

1. [MATLAB. Publishing Markup](http://de.mathworks.com/help/matlab/matlab_prog/marking-up-matlab-comments-for-publishing.html). An overview of MATLAB Publishing Markup with its options and a wide selection of examples.
2. [Publishing MATLAB Code](http://de.mathworks.com/help/matlab/matlab_prog/publishing-matlab-code.html). A short example using many Markup options within a formatted file, that generates a documentation of the code.
3. [MATLAB. Markup Help](http://www.mathworks.com/matlabcentral/answers/help/markup/). Very short MATLAB Markup help with the highlights of its functionality.
4. [MATLAB. Add Help for Your Program](http://de.mathworks.com/help/matlab/matlab_prog/add-help-for-your-program.html). The exaplanation of a **help text** in an M-file. This text appears when the keyword `help`  is typed before the name of a function in the Command Window.