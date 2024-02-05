import React from "react";
import NavBar from './NavBar'

export default function HomePage() {
    return (
        <div>
            <NavBar />
            <div className="flex justify-center items-center font-bold text-3xl mt-10">
                Automated Inventory Processing System
            </div>
            <div className="flex justify-center items-center font-bold text-2xl mt-2">
                Seamlessly Update Your&nbsp;<span className="text-red-500">Inventory</span>
            </div>
        </div>
    );
}

