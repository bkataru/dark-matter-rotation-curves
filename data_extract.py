
def extract_galaxy_data(filename):
    fileid = filename.split('.')[0]

    gdata = {
        "fileid": fileid,
        "data": []
    }

    with open(filename) as input_file:
        for line in input_file:
            if line.startswith("#"):
                if line.find(":") != -1:
                    line = line.split("#")[1]
                    line = [elem.strip() for elem in line.split(":")]
                    if len(line) > 1:
                        gdata[line[0]] = line[1]
                else:
                    line = [elem.strip() for elem in line.split(" ")[1:] if len(elem.strip()) > 0]
                    if len(line) > 0:
                        gdata["data"].append(tuple(line))

            else:
                line = [elem.strip() for elem in line.split(" ") if len(elem.strip()) > 0]
                if len(line) > 0:
                    gdata["data"].append(tuple(line))

    data = dict()     
    for idx in range(len(gdata["data"][0])):
        param = gdata["data"][0][idx]
        param_data = []
        for elem in gdata["data"][1:]:
            param_data.append(elem[idx])
        
        data[param] = param_data

    gdata["data"] = data

    return gdata
