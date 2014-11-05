def tabularize(lines, spacing=2):
    def format_border(widths):
        return spc.join([ '=' * width for width in widths ])

    def format_header(header, widths, spc):
        border = format_border(widths)
        header = spc.join(map(lambda col, width: col.ljust(width),
                              header, widths)).rstrip()
        return '\n'.join([border, header, border])

    def sort_by_col(lines, col):
        return sorted(lines, key=lambda l: l[col])

    def format_body(lines, widths, spc):
        def format_line (line):
            return spc.join(map(lambda col, width: col.ljust(width),
                                line, widths)).rstrip()
        return "\n".join(map(format_line, sort_by_col(lines, 0)))

    spc = ' ' * spacing
    if lines:
        col_widths = map(lambda col: apply(max, map(len, col)),
                         apply(zip, lines))
        return '\n'.join([format_header(lines[0], col_widths, spc),
                          format_body(lines[1:], col_widths, spc),
                          format_border(col_widths)]) + \
               '\n'
    else:
        return ""
