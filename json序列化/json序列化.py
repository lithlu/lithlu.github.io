# Author:Lithlu
import json
info = {
    "name":"lithlu",
    "age":21
}
f = open("test.text","w")
f.write(json.dumps(info))
f.close()