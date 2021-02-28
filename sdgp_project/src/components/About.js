import React from 'react';
import img1 from '../images/about.png'
import img2 from '../images/goal.png'
import img3 from '../images/vithushigan.jpg'

export const About = () => (
    <div calss = "container">
    <div class = "jumbotron">
        <h1>
            About Us
        </h1>
        <div>
        <img src= { img1 } class="rounded" alt="about" style={{width: 600, height: 400}}></img>
        </div>  
    </div>

    <div class = "jumbotron text-right">
        <h1>
            Goal of our project
        </h1>
        <img src= { img2 } class="rounded" alt="goal" style={{width: 700, height: 400}}></img>

    </div>

    <div class = "">
        <h1>The Team Memebers</h1>
        <div class = "row">

            <div class = "col-sm-6">
                <div class="card" style={{width: 300}}>
                    <img src=  {img3} style={{ width: 300 , height: 300}}  alt="Thuwarakan "></img>
                    <div class="card-body">
                        <h3 class="card-title">J. Thuwarakan</h3>
                        <p>IIT ID: 2019795</p>
                        <p>UoW ID: W1790265</p>
                    </div>
                </div>
            </div>
                
            <div class = "col-sm-6">
                <div class="card" style={{width: 300}}>
                    <img src= {img3} style={{ width: 300 , height: 300}}  alt="Ben "></img>
                    <div class="card-body">
                        <h3 class="card-title">C. S. Benhanan</h3>
                        <p>IIT ID: 20191203</p>
                        <p>UoW ID: W1790312</p>
                    </div>
                </div>
            </div>
            
            <div class = "col-sm-6">
                <div class="card" style={{width: 300}}>
                    <img src= {img3} style={{ width: 300 , height: 300}}  alt="Vithushigan "></img>
                    <div class="card-body">
                        <h3 class="card-title">J. Vithushigan</h3>
                        <p>IIT ID: 20191148</p>
                        <p>UoW ID: W1790018</p>
                    </div>
                </div>
            </div>
                
            <div class = "col-sm-6">
                <div class="card" style={{width: 300}}>
                    <img src= {img3} style={{ width: 300 , height: 300}}  alt="Niragulan "></img>
                    <div class="card-body">
                        <h3 class="card-title">S. Niragualn</h3>
                        <p>IIT ID: 20191022</p>
                        <p>UoW ID: W1790287</p>
                    </div>
                </div>
            </div>

            <div class = "col-sm-6">
                <div class="card" style={{width: 300}}>
                    <img src= {img3} style={{ width: 300 , height: 300}}  alt="Jenoshanan "></img>
                    <div class="card-body">
                        <h3 class="card-title">M. Jenoshanan</h3>
                        <p>IIT ID: 2019695</p>
                        <p>UoW ID: W1790160</p>
                    </div>
                </div>
            </div>

            <div class = "col-sm-6">
                <div class="card" style={{width: 300}}>
                    <img src= {img3} style={{ width: 300 , height: 300}}  alt="Ashwinth "></img>
                    <div class="card-body">
                        <h3 class="card-title" class="card-header">R. Ashwinth</h3>
                        <p>IIT ID: 2019713</p>
                        <p>UoW ID: W1790169</p>
                    </div>
                </div>    
            </div>

        </div>
    </div>
</div>
);