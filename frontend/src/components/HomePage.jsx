import React from "react";
import NavBar from './NavBar'
import InstructionBar from './InstructionBar'

function Button(props) {
    return (
        <button className="font-bold text-sm bg-red-default text-white-default px-4 py-3 mx-7 hover:bg-red-bg rounded-2xl transition duration-300 ease-in-out overflow-hidden whitespace-nowrap">
            {props.children}
        </button>
    );
  }

export default function HomePage() {
    return (
        <div>
            <div>
                <NavBar />
                <div className="flex justify-center items-center font-bold text-3xl mt-10">
                    Automated Inventory Processing System
                </div>
                <div className="flex justify-center items-center font-bold text-2xl mt-2">
                    Seamlessly Update Your&nbsp;<span className="text-red-default">Inventory</span>
                </div>
                <div className = "flex justify-center items-center mt-8">
                    <Button>Get Started</Button> 
                    <Button>Testimonials</Button>
                </div>
            </div>

            <div>
                <InstructionBar />
            </div>
        </div>
    );
}

