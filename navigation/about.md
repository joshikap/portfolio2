---
layout: post
title: About
permalink: /about/
comments: true
---

## As a conversation Starter

Here are some places I have lived.

<comment>
Flags are made using Wikipedia images
</comment>

<style>
    /* Style looks pretty compact, 
       - grid-container and grid-item are referenced the code 
    */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
    }
    .grid-item {
        text-align: center;
    }
    .grid-item img {
        width: 100%;
        height: 100px; /* Fixed height for uniformity */
        object-fit: contain; /* Ensure the image fits within the fixed height */
    }
    .grid-item p {
        margin: 5px 0; /* Add some margin for spacing */
    }

    .image-gallery {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 10px;
        }

    .image-gallery img {
        max-height: 150px;
        object-fit: cover;
        border-radius: 5px;
    }
</style>

<!-- This grid_container class is used by CSS styling and the id is used by JavaScript connection -->
<div class="grid-container" id="grid_container">
    <!-- content will be added here by JavaScript -->
</div>



<script>
    // 1. Make a connection to the HTML container defined in the HTML div
    var container = document.getElementById("grid_container"); // This container connects to the HTML div

    // 2. Define a JavaScript object for our http source and our data rows for the Living in the World grid
    var http_source = "https://upload.wikimedia.org/wikipedia/commons/";
    var living_in_the_world = [
        {"flag": "0/01/Flag_of_California.svg", "greeting": "Hey", "description": "California - forever"},
    ];

    // 3a. Consider how to update style count for size of container
    // The grid-template-columns has been defined as dynamic with auto-fill and minmax

    // 3b. Build grid items inside of our container for each row of data
    for (const location of living_in_the_world) {
        // Create a "div" with "class grid-item" for each row
        var gridItem = document.createElement("div");
        gridItem.className = "grid-item";  // This class name connects the gridItem to the CSS style elements
        // Add "img" HTML tag for the flag
        var img = document.createElement("img");
        img.src = http_source + location.flag; // concatenate the source and flag
        img.alt = location.flag + " Flag"; // add alt text for accessibility

        // Add "p" HTML tag for the description
        var description = document.createElement("p");
        description.textContent = location.description; // extract the description

        // Add "p" HTML tag for the greeting
        var greeting = document.createElement("p");
        greeting.textContent = location.greeting;  // extract the greeting

        // Append img and p HTML tags to the grid item DIV
        gridItem.appendChild(img);
        gridItem.appendChild(description);
        gridItem.appendChild(greeting);

        // Append the grid item DIV to the container DIV
        container.appendChild(gridItem);
    }
</script>

### Journey through Life

Here is what I like to do in California

-Go to the beach (swimming, tide pools, watching the sunset, building sand castles)

-Hike local trails or state parks (My favorite is the Ho Chi Minh Trail in Torrey Pines)

-Visit redwood forests and see trees taller than buildings

-Have a picnic with friends at a beach

-Hang out with my friends and family in downtown

-Playing tennis and going to tournaments



### Journey through Life

<div class="journey-gallery" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 20px 0;">
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/68/Los_Angeles_%28California%2C_USA%29%2C_South_Olive_Street_--_2012_--_4847.jpg" alt="Image 1 Description" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
    <p style="margin-top: 10px; font-weight: bold;"> </p>
  </div>
  
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/5/50/Tennis_court_at_Grindleford_-_geograph.org.uk_-_571857.jpg" alt="Image 2 Description" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
    <p style="margin-top: 10px; font-weight: bold;"> </p>
  </div>
  
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/8/8d/20100524_Kardamos_beach_Imbros_G%C3%B6k%C3%A7eada_Turkey.jpg" alt="Image 3 Description" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
    <p style="margin-top: 10px; font-weight: bold;"> </p>
  </div>
</div>


### Culture, Family, and Fun

- I have lived in San Diego since I was born
- I live with my two sisters, and my mom and dad 

Hindu culture is ancient and diverse, centered around values like dharma (doing what’s right), karma (actions have consequences),  and balance in life. It includes many traditions, languages, and ways of practicing, but family and community are common themes. Festivals such as Diwali, Holi, and Navratri, celebrate light over darkness, joy, and family bonds. Practices like yoga, meditation, prayer, and food connect mind, body, and spirit. Hindu stories, music, dance, and symbols teach lessons about courage, kindness, and self-understanding. For many Hindu teens, especially in places like California, the culture is a blend of tradition at home and modern life outside, creating a unique identity.


### Favorite desserts 

<div id="grid_container2"></div>



<script>
    var outputElement = document.getElementById
    ("grid_container2");

// Clear the output
outputElement.innerHTML = '';

// Data array
const favorites = [
  {flag: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Classic_Italian_Tiramisu-3_%2829989504485%29.jpg/640px-Classic_Italian_Tiramisu-3_%2829989504485%29.jpg", description: "Tiramisu is my favorite cake."},
  {flag: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/French_macaroons.jpg/640px-French_macaroons.jpg", description: "Macarons are my faborite cookie."},
  {flag: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Croissants_au_beurre_%2818953292873%29.jpg/640px-Croissants_au_beurre_%2818953292873%29.jpg", description: "Croissants are my favorite type of pasteries."},
  {flag: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Chocolate_ice_cream_%282009-01-07%29.jpg/640px-Chocolate_ice_cream_%282009-01-07%29.jpg", description: "Chocolate is my favorite flavor of ice cream."}
];


// Create a div container2 with id
const container2 = document.createElement('div');
container2.id = 'grid_container';

// Style the container2
container2.style.border = '2px solid';
container2.style.padding = '10px';

// Grid specific styles
container2.style.display = 'grid';
container2.style.gridTemplateColumns = 'repeat(auto-fill, minmax(150px, 1fr))';
container2.style.gap = '10px';

// Loop through data and create grid items
for (const location of favorites) {
  // Create grid item
  const gridItem = document.createElement('div');
  gridItem.style.textAlign = 'center';
  
  // Create a flag image
  const img = document.createElement('img');
  img.src = location.flag;
  img.alt = location.description + ' Flag';
  img.style.width = '100%';
  img.style.height = '100px';
  img.style.objectFit = 'contain';
  
  // Create a description
  const description = document.createElement('p');
  description.textContent = location.description;
  description.style.margin = '5px 0';
  description.style.fontWeight = 'bold';
  
  // Create a greeting
  const greeting = document.createElement('p');
  greeting.textContent = location.greeting;
  greeting.style.margin = '5px 0';
  greeting.style.fontStyle = 'italic';
  greeting.style.opacity = '0.7';
  
  // Add all elements to grid item
  gridItem.appendChild(img);
  gridItem.appendChild(description);
  gridItem.appendChild(greeting);
  
  // Add grid item to container2
  container2.appendChild(gridItem);
}

// Add containter to output 
outputElement.appendChild(container2);

</script>



