import React from "react";

function NavBar() {
    return (
        <div className="flex justify-center pt-6">
            <nav className="inline-flex justify-center items-center bg-zinc-800 rounded-full ">
                <button className="font-bold text-sm text-zinc-400 px-4 py-2 mx-5">support</button>
                <div className="font-bold text-xl text-red-600 px-4 py-2">AIPS</div>
                <button className="font-bold text-sm text-zinc-400 px-4 py-2 mx-5">login</button>
            </nav>
        </div>
    );
}

export default NavBar;
