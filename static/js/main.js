
$(function () {
  console.log("It's working!!!!!")

  //Variables
  let $oldName = $('#oldName');
  let $nameForm = $('#nameForm');
  let $newName = $('#name');
  let $taglineForm = $('#taglineForm');


  //Functions to get Cool Things on Forms

  //Takes the vowels out of a string
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

  // Get info from Name Field & Place in the Startup Form
  function getRouletteName(evt) {
    evt.preventDefault();
    let rouletteName = shortcut($oldName.val())
    console.log(rouletteName)
    $newName.val(rouletteName)
  };




  // Run function to get new Name
  $nameForm.on('submit', getRouletteName)
  //Set value for form tag as the new name
  //Generate Tagline for new name using function from before

  //API call to the Unsplash API to get an image that matches one of the nouns


});
