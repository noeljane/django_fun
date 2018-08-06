
$(function () {
  console.log("It's working!!!!!")

  //Variables
  let $oldName = $('#oldName');
  let $nameForm = $('#nameForm')


  $nameForm.on('submit', getNewName)

  //This function takes the vowels out of a string
  function shortcut(string) {
    let newString = ""
    let vowels = ['a', 'e', 'i', 'o', 'u']
    for (let i = 0; i < string.length; i++) {
      if (!vowels.includes(string[i])){
        newString += string[i]
      }
    }
    return newString
  };

  // Get info from Name Field
    //Write function that obtains the value of the input in the form
    //set variable of name to pass to the shortcut function
  function getNewName(evt) {
    evt.preventDefault()
    console.log("I'm running a function now.");
    

  };



  // Run function to get new Name
  //Set value for form tag as the new name
  //Generate Tagline for new name using function from before

  //API call to the Unsplash API to get an image that matches one of the nouns


});
