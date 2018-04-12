// This webapp gets the rss feed from www.arxiv.org and offers it up in plain text to whoever requests it.
// Conceived as a workaround because arxiv.org was originally not on pythonanywhere's whitelist.

deployedurl = 'https://script.google.com/macros/s/AKfycbxnCZaPPxwOKm8Q6i-XWkJ1gxx8a4bLB3T85mBk6LGj7koQqbDz/exec'

function doGet(e) {
  
  for (param in e.parameters){
    Logger.log('param: ' + param)
    
    if(param == 'url'){
      site = e.parameters[param][0]
      Logger.log('site: ' + site)
      if(site.substring(0, 17) == 'https://arxiv.org'){
        Logger.log('valid arxiv site')
        var stuff = UrlFetchApp.fetch(site)
        Logger.log('stuff: ' + stuff.getContentText())
        return ContentService.createTextOutput(stuff.getContentText()).setMimeType(ContentService.MimeType.RSS);
      }
    }
  } 
  failure_message = 'No valid arxiv site requested'
  Logger.log(failure_message)
  return ContentService.createTextOutput(failure_message);
}

function test() {
  response = doGet({"parameters":{
    'url':['https://arxiv.org/abs/1804.01913']
    //'url':['www.brown.edu']
  }})
  Logger.log(response)
}