
$(function () {


  //Variables
  let $oldName = $('#oldName');
  let $nameForm = $('#nameForm');
  let $newName = $('#name');
  let $taglineForm = $('#taglineForm');
  let $newTagline = $('#tagline')

  let $noun = $('#noun')

  



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

  //Generate Tagline for new name using function I wrote before:
  var startups = ["Uber", "AirBnb", "Tinder", "Grindr", "Shazam", "Pandora", "Spotify", "Instagram", "Facebook", "MySpace", "Rover", "Blue Apron", "SnapChat", "Google" ]

  //Make a Random Number Function

  function randomNumber(num){
    return Math.floor((Math.random() * num))
  };


  function makeTagline (){

    let i = randomNumber(startups.length)
    let startupName = startups[i]

    return `${startupName} for ${$noun.val()}`

  };

  // Get info from Name Field & Place in the Startup Form
  function getRouletteStartup(evt, userNoun) {
    evt.preventDefault();
    let rouletteName = shortcut($oldName.val());
    let rouletteTagline = makeTagline($noun.val());
    //Set value for form tag as the new name
    $newName.val(rouletteName);
    $newTagline.val(rouletteTagline);
    
  };


  // Run function to get new Name
  $nameForm.on('submit', getRouletteStartup);


  //API call to the Unsplash API to get an image that matches one of the nouns
  
      //To Finish API Request: 
      //Figure out how to get client id from the back end to the front end using settings.py and .env
      //Figure out how to get a random photo populate when you make the ajax request (ie generate a random number from the length of the array in the json response)
      //post that image to the screen
      //make it so you can click things separately. 
    
    
   

  

});
