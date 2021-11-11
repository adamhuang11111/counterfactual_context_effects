function download(json, filename){
  var jsonFile
  var downloadLink
  jsonFile = new Blob([json], {type:"text/json"})
  downloadLink = document.createElement( tagName = "a")
  downloadLink.download = filename;
  downloadLink.href = window.URL.createObjectURL(jsonFile)
  downloadLink.style.display - 'none'
  document.body.appendChild(downloadLink)
  downloadLink.click()
}