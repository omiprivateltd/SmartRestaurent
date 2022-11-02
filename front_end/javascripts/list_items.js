function call_api() { 
    // Function Used to get all items in database
    api_endpoint = "http://127.0.0.1:8000/getItems?html=True"
    fetch(api_endpoint,{method:"GET"}).then(response => response.json()).then(response => handle_api_response(response))  
}

function handle_api_response(response) { 
    // Function Used to handle api response
    let menu_holder = document.getElementById("menu-holder")
    if (response.length==0) {alert("NO ITEM FOUND IN DATBASE PLEASE ADD SOME MORE ITEM")}
    response.forEach(element => { 
    let to_insert = document.createElement("div")
    to_insert.innerHTML = element
    menu_holder.append(to_insert)
    
   });

}