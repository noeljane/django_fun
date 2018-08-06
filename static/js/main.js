
$(function () {
  console.log("It's working!!!!!")

  //Variables
  let $oldName = $('#oldName')
  console.log($oldName.val());

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


  // Run function to get new Name
  //Set value for form tag as the new name
  //Generate Tagline for new name using
});
