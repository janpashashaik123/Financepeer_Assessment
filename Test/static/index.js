window.addEventListener('load', function() {
  var upload = document.getElementById('file');
  var filepath=upload.value;
  var allowedExtension=/\.(json)$/i;
  if (!allowedExtension.exec(filepath))
  {
    alert('Invalid File type');
    upload.value='';
    return false;
  }
  else
  {
    if (upload) 
    {
      upload.addEventListener('change', function() {
        // Make sure a file was selected
        if (upload.files.length > 0) 
        {
          var reader = new FileReader(); // File reader to read the file 
          
          // This event listener will happen when the reader has read the file
          reader.addEventListener('load', function() {
            var result = JSON.parse(reader.result); // Parse the result into an object 
            
            console.log(result);
            console.log(result.name);
            console.log(result.age);
            console.log(result.occupation);
          });
          
          reader.readAsText(upload.files[0]); // Read the uploaded file
        }
      });
    }
}
});