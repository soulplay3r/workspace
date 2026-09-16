import About from "./components/About";
import AILab from "./components/AILab";
import Beyond from "./components/Beyond";
import Builds from "./components/Builds";
import Contact from "./components/Contact";
import Footer from "./components/Footer";
import Hero from "./components/Hero";
import HowIThink from "./components/HowIThink";
import Nav from "./components/Nav";
import ProofStrip from "./components/ProofStrip";
import WhatIBuild from "./components/WhatIBuild";
import Work from "./components/Work";
import Writing from "./components/Writing";

export default function App() {
  return (
    <>
      <Nav />
      <main>
        <Hero />
        <ProofStrip />
        <WhatIBuild />
        <Work />
        <Builds />
        <AILab />
        <HowIThink />
        <About />
        <Writing />
        <Beyond />
        <Contact />
      </main>
      <Footer />
    </>
  );
}
