# Concept paper
* impact -- *disruptive*
* figure
* methanol economy better than hydrogen
* incremental market introduction
* target energy density (volumetric & gravimetric)
* address <math xmlns="http://www.w3.org/1998/Math/MathML">
        <mn>C</mn>
        <msub><mn>O</mn><mn>2</mn></msub>
    </math>

## Task assignment
* manufacturing: PGI
* battery development/selection: Chunmei
* Stabilize Pt:Ru catalyst: Steve
* Methanol concentration/crossover (MEA): Branden

## Outline/scratch

*Opening Line* Since their inception 25 years ago, direct methanol fuel cells have struggled to live up to the promise evident in a renewable fuel source that carries ten times the energy density of compressed hydrogen and fifteen times that of lithium ion batteries. With developments in membrane and catalyst technologies, this is poised to change.

Despite their strengths, all fuel cells -- including direct methanol -- suffer from intrinsic electrochemical limitations to their use as stand-alone power supplies. Sluggish kinetics and chemical, mass transport, and ohmic polarization losses impede their ability to promptly respond to changes in power demand and result in a narrow power band, respectively.

Where fuel cells fall short, batteries excel. Their ability to respond instantly to changing power demands and their wide power band, extending over several orders-of-magnitude in their operational C-rate, is a succor for the problems facing fuel cells. However, even state-of-the-art lithium ion batteries fall well short of the energy density available from methanol.

We propose a hybrid battery-fuel cell power system that joins the energy density and generation properties of a fuel cell with the power response of batteries; leveraging the strengths of the one in support of the weaknesses of the other.

Such a system also provides an important flexibility in design. Under the paradigm of this hybrid power-system, the average power demand, $\langle \mathrm{power} \rangle \times \textrm{duty cycle}$, dictates the power capacity of the fuel cell, while deviation from this average dictates the capacity of the battery. Designs that minimize these fluctuations, and improvements in electrochemical energy storage serve to reduce the weight, and volume, of the battery: a volume that can be repurposed to provide more fuel. At fifteen times greater energy density, combining energy generation and energy storage leverages developments in either into a capacity multiplier.

<!-- The choice of fuel cell and battery technologies are an optimization that requires careful consideration of application-specific demands. --!>

This project will focus on the low-to-mid-level power requirements of portable power, with near-term implications in the transportation (EV) market.

### Fuel Cell
There are many fuel cell technologies available: hydrogen, direct alcohol, molten carbonate, solid oxide.

The scalability of fuel cells decouples power and energy capacity.

* Type of fuel cell

    * low T: hydrogen, direct methanol, set fuel type, but more efficient for both small scale and intermittent applications.
    
    * high T: molten carbonate, solid oxide, flexible fuel, but inefficient for small scale and intermittent applications.
    
* Hydrogen vs. methanol

    * Methanol and hydrogen have comparable energy capacities. [(Arico2009)][Arico2009]  
    <table>
        <tr>
            <th>Fuel</th>
            <th>Energy Density<br>(Wh/L)</th>
            <th>Specific Energy<br>(Wh/kg)</th>
        </tr>
        <tr>
            <td>Methanol</td>
            <td>3228 - 3976</td>
            <td>5390 - 7122</td>
        </tr>
        <tr>
            <td>hydrogen<br>(metal hydride)</td>
            <td>1532 - 2339</td>
            <td>374 - 635</td>
        </tr>
        <tr>
            <td>hydrogen<br>(cryogenic liquid)</td>
            <td>1839 - 2317</td>
            <td>25,316 - 33,172</td>
        </tr>
    </table>  
    Although liquid hydrogen provides the largest gravimetric capacity, this is overshadowed by the balance of plant structures required for cryogenic storage (reference?). Methanol has a 75.5% higher energy density than cryogenic hydrogen and a negligible intrinsic requirement for fuel storage.
    
    * Existing manufacturing, distribution, and point-of-sale infrastructure can be easily, and incrementally, converted from gasoline/diesel to methanol. Hydrogen could not.
    
    * Currently, (fraction?) methanol is produced by steam reforming methane (reference?). However unlike other higher order alcohols, technologies exist at a technological readiness level of XX for the commercial production of methanol from biomass. Thus, the use of methanol would result in the closed cycle production, distribution, and reclamation of carbon, resulting in a carbon-neutral fuel source.

For these reasons, this work will focus on the integration of direct methanol fuel cells as the power generator.

### Batteries
There are many energy storage options: lithium ion, magnesium ion, redox flow, supercapacitors. (Expand discussion on the down selection from these to lithium ion batteries.)

With volumetric energy densities between 256 and 394 Wh/L and specific energies between 86 and 147 Wh/kg,[(Arico2009)][Arico2009] lithium ion batteries have energy capacities and kinetics sufficient to handle fluctuations in power demands.

The use of liquid electrolytes in lithium ion battery chemistries increases the complexity of battery design and are involved in numerous unsafe redox reactions, particularly at overcharged and undercharged conditions. Solid state lithium ion batteries do not suffer from operational limitations that plague these chemistries.

A hybrid power systems ensures the battery remain within the broad window for optimal battery performance.

For these reasons, this work will focus on integration of solid state lithium ion batteries as the power storage medium.

## References
(Arico2009) Aric&ograve;, A., Baglio, V. & Antonucci, V. in Electrocatal. Direct Methanol Fuel Cells 1-78 (2009)
[Arico2009]: http://books.google.com/books?hl=en&lr=&id=xHsJJieZlHwC&oi=fnd&pg=PA1&dq=Direct+Methanol+Fuel+Cells+:+History+,+Status+and+Perspectives&ots=iDVDBBaEl5&sig=BtotK4fVYetE5w_cc2AigTz2Dnk "Aric&ograve;, A., Baglio, V. & Antonucci, V. in Electrocatal. Direct Methanol Fuel Cells 1-78 (2009)."

# Notes

## Lit. Notes

0. Methanol as a renewable fuel source: Liu2006; Wasmus and Kuver, J. Electroanal. Chem 461 (1999) 14-31; Arico, et al., Fuel Cells 2 (2001) 133-161

1. Methanol electrooxidation steps: (1) methanol adsorption, (2) C--H activation (methanol dissociation), (3) water adsorption, (4) water activation, (5) CO oxidation; Lemy, Leger, and Srinivasan, Modern Aspects of Electrochem 34 (2001) 53-118

2. Mench2003, ORR is the limiting reaction, how significantly? Other papers state that the anode catalyst is the limiting factor -- perhaps longevity? -- which stands in opposition to this assertion.

3. Burke2007: simulations show hybrid hydrogen FC/battery-or-supercap EVs have 2-3 times the fuel economy of gasoline IC and 1.66-2x than gas-electric hybrids. NREL Advisor program? INEL SIMPLEV program for FC/batt hybrid.

4. Shimozu2004: Directly on point, passive DMFC operating at room temperature, but performance metrics are not ideal, and demonstrate the narrow window of optimal FC operation.

5. Gauchia2011: hydrogen FC/electrochemical storage concept. Directly on point. This work shows a model of a hybrid system, but uses the FC to directly power the vehicle. Our device separates the FC from the system power requirements, thus ensuring better control over battery SOC and fuel cell operating conditions.

6. Feng2013: catalyst particle dispersion and support are important inf electrochem. performance.

7. Zheng2012: MEA production and catalyst loading are the two outstanding challenges that impede commercialization of DMFC.

8. Joghee2012: Nitrogenation of MEA stabilizes Pt:Ru catalyst.

9. Tateishi2013: GO-only fuel cell membrane. Low temperature <28 C and very low power densities, energy densities and high polarization.

## Benefits

A hybrid system allows the strengths of one component to balance the weaknesses of the other, e.g.

1. developments in energy storage (battery), energy production (fuel cell), methanol production and distribution -- and to a lesser degree, DC power electronics -- provide independent pathways to system improvement and incorporation.

2. methanol distribution can be incorporated into existing infrastructure with minimal effort. This allows methanol production and distribution to be ramped up incrementally.

### DMFC
* extensible energy capacity
* high energy density (volumetric and gravimetric) than lithium ion
	hydrogen.
* existing potential for a closed carbon cycle fuel
* excellent scalability
* excellent cell-to-cell consistency

### Batt
* rapid power response (kinetics)
* medium capacity (SC < Batt < DMFC)

Several technical challenges prevent immediate implementation of a HBFC...

## Technical Challenges

### DMFC
* poor kinetics
* catalyst stability (anode)
* crossover current
	* electromigration
	* diffusion
* polarization
	* Ohmic
	* electrochemical
	* catalytic
* <math xmlns="http://www.w3.org/1998/Math/MathML">
        <msub><mn>H</mn><mn>2</mn></msub>
        <mn>O</mi>
    </math> management
* DC electronics require
    <math xmlns="http://www.w3.org/1998/Math/MathML">
        <mn>V</mn><mo>&ge;</mo><mn>1 V</mn>
    </math>

### Battery
* limited energy storage capacity
* poor operating range (T, state of charge -- charge window)
