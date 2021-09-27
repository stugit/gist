# gist

```
def updateEmailCandidate(file_contents, run_name, run_times) {
count = 0
run_times.each {
t->
count_string = count.toString().padLeft(3, "0")
start_key = "[" + run_name + "_starttime" + count_string + "]"
file_contents = file_contents.replace(start_key, t["start_time"])
end_key = "[" + run_name + "_endtime" + count_string + "]"
file_contents = file_contents.replace(end_key, t["end_time"])
end_time_parsed = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").parse(t["end_time"])
start_time_parsed = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").parse(t["start_time"])
// duration is in ms (getTime() returns the Epoch in ms)
duration = end_time_parsed.getTime() - start_time_parsed.getTime()
duration = (duration / 1000 / 60).intValue()
duration_key = "[" + run_name + "_duration" + count_string + "]"
file_contents = file_contents.replace(duration_key, duration.toString())
++count
}
return file_contents
}

def generateEmail() {
filename = "message.html"
data = "test_build/data/pricing_baseline_run.json"
template = "test_build/templates/table1.template"
def props = readJSON(text: readFile(data), returnPojo: true)
def file_contents = readFile(template)
props.each { key, value -> file_contents = updateEmailCandidate(file_contents, key, value)}
writeFile(file: filename, text: file_contents)
return filename
}
```
# dummy
