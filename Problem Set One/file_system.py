# Decodes a path string, constructs a file path and return the longest file path

def decode(s):
    nodes = {}
    active_parent = None
    tcount = 0
    while 1:
        try:
            index = s.index("\n")
            node = s[:index]
            s = s[index:]
            nodes[node] = active_parent
        except:
            index = len(s)
            node = s[:index]
            s = ""
            nodes[node] = active_parent
            break

        sep = separator_str(s)
        new_t_count = sep.count("\t")
        if new_t_count > tcount:
            active_parent = node
            tcount = new_t_count
            s = s.replace(sep, "", 1)
        elif new_t_count < tcount:
            active_parent = nodes[active_parent]
            tcount = new_t_count
            s = s.replace(sep, "", 1)
        else:
            s = s.replace(sep, "", 1)
    return nodes
def separator_str(s):
    separator = ""
    start = 0
    end = 1
    while s[start:end] in "\n\t":
        separator += s[start:end]
        start = end
        end = start + 1
    return separator

def longest_path(s):
    nodes = decode (s)
    file_nodes = dict(filter(lambda x: len(x[0]) > 4 and x[0][-4] == ".", nodes.items()))
    if file_nodes:
        return max([len(absolute_path(nodes, node)) for node in file_nodes])
    else:
        return 0

def absolute_path(nodes, file):
    path = file
    parent = nodes[file]
    while (parent):
        path = parent + "/" + path
        parent = nodes[parent]
    return path

print(longest_path("file1.txt\nfile2.txt\nlongfile.txt"))

# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"



