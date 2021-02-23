import React from 'react';
import Welcome from './welcome/Welcome';
import About from './about/About';
import Navbar from '../navbar/Navbar';
import Footer from '../footer/Footer';

class Home extends React.Component{
    render(){
        return (
            <div>
                <Navbar/>
                <Welcome/>
                <About/>
                <Footer/>
            </div>
        );
    };
}
export default Home;