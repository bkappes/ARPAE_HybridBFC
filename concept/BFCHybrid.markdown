# A Direct Methanol Fuel Cell-Solid State Lithium Ion Battery Hybrid Power System for Portable Applications

<div align="center">
  Branden B. Kappes<sup>1,2</sup>,
  Cristian V. Ciobanu<sup>2</sup>,
  Chunmei Ban<sup>3</sup>,
  Steven Christensen<sup>3</sup>,
  Katherine Hurst<sup>3</sup><br />
  <sup>1</sup>Process Group International, Livermore, CA<br />
  <sup>2</sup>Department of Mechanical Engineering, Colorado School of Mines, Golden, CO<br />
  <sup>3</sup>National Renewable Energy Laboratory, Golden, CO
</div>

## Introduction

Since their inception 25 years ago, direct methanol fuel cells have struggled to live up to the promise evident in a renewable fuel source that carries ten times the energy density of compressed hydrogen and fifteen times that of lithium ion batteries. With developments in membrane and catalyst technologies, this is poised to change.

Despite their strengths, all fuel cells -- including direct methanol -- suffer from intrinsic electrochemical limitations to their use as stand-alone power supplies. Sluggish kinetics and chemical, mass transport, and ohmic polarization losses impede their ability to promptly respond to changes in power demand and result in a narrow optimal operating range, respectively.

Where fuel cells fall short, batteries excel. Their ability to respond instantly to changing power demands and their wide power band, extending over several orders-of-magnitude in their operational C-rate, is a succor for the problems facing fuel cells. However, even state-of-the-art lithium ion batteries fall well short of the energy density available from methanol.

We propose a hybrid battery-fuel cell power system that joins the energy density and generation properties of a fuel cell with the power response of batteries; leveraging the strengths of the one in support of the weaknesses of the other.

Such a system provides an important flexibility in design. Under the paradigm of this hybrid power-system, the average power demand, $\langle \mathrm{power} \rangle \times \textrm{duty cycle}$, dictates the power capacity of the fuel cell, while deviation from this average dictates the battery capacity. Designs that minimize these power fluctuations, and improvements in electrochemical energy storage serve to reduce the weight, and volume, of the battery: a volume that can be repurposed to provide more fuel. At fifteen times greater energy density, combining energy generation and energy storage leverages developments in either into a capacity multiplier.

<!-- The choice of fuel cell and battery technologies are an optimization that requires careful consideration of application-specific demands. -->

This project will focus on the low-to-mid-level power requirements of portable power, with near-term implications in the transportation (EV) market.

## Fuel Cell
The scalability of fuel cells decouples power and energy capacity, and enables use of fuels with very high energy densities, as compared to exisiting electrochemical energy storage options.

The first reported fuel cell dates back to work by W.R. Grove in 1838 [(Grove1838)][Grove1838], who a year later, introduces platinum to catalyze the hydrogen oxidation and oxygen reduction reactions [(Grove1839)][Grove1839].

Since then, many fuel cell technologies have been developed, and are frequently categorized by their electrolyte, e.g. PEM (proton exchange membrane, or polymer electrolyte membrane), phosphoric acid, molten carbonate, and solid oxide fuel. Practically, these may also be classified by their respective operating temperatures.

Molten carbonate and solid oxide fuel cells require temperatures above 600 &deg;C to enable sufficient anion mobility, $\mathrm{CO_3^{2-}}$ and $\mathrm{O^{2-}}$, respectively. These temperatures enable significant fuel flexibility without need for an external reformer and facilitates both the fuel oxidation and oxygen reduction reactions; however, system component longevity is a persistent problem at these elevated temperatures. Additionally, cyclic usage patterns result in thermal cycling that requires careful matching of thermal expansion coefficients for both structural and active components, e.g. seals, electrodes, casing, etc. This constraint severely limits materials options for these components. Additionally, heat loss varies inversely with system size, and cogeneration facilities that make use of waste heat are cumbersome to integrate into compact, mobile systems. These constraints make high temperature fuel cells less attractive for portable applications.

At an operating temperature of 150-200 &deg;C, phosphoric acid fuel cells do not suffer from the same thermal management problems as high temperature fuel cells, but containing the highly corrosive electrolyte at elevated temperature similarly limits longevity and poses a safety concern in a consumer device. Furthermore, to increase the capacity of these fuel cells by only 20% would require significant advancements in reducing anion adsorption at the low-index planes of the Pt catalyst [(Rimick2010a)][Rimick2010a], [(Mench2003)][Mench2003].

PEM operate below 100 &deg;C, which makes this class of fuel cells highly attractive for portable applications. The low temperature operation does limit both the chemical and mass transport kinetics, leading to appreciable polarization losses, but recent developments in membrane technology may significantly reduce both the mass transport polarization and the reduced operating potential that results from fuel crossover [(Tateishi2013)][Tateishi2013]. Furthermore, the low operating temperature minimizes thermal management concerns for portable applications, and reduces thermal energy losses associated with operation cycling.

Of the potential PEM fuels, compressed and liquid hydrogen have received significantly more attention.

<figure>
  <a href="fig/publication_count.png">
      <img src="fig/publication_count.png" alt="publication count">
  </a>
  <figcaption>
Number of publications that reference "hydrogen fuel cell" or "direct alcohol methanol fuel cell", according to *scholar.google.com*. Accessed: 12 February 2015.
  </figcaption>
</figure>

Despite over a century of additional research and a more extensive track record of recent investigation, hydrogen fuel cells still share many of the same barriers to commercialization as direct methanol, but methanol is more easily stored, can, unlike hydrogen, be readily integrated into the existing liquid fuels distribution infrastructure, and has notably higher energy capacities.

<table>
  <caption>
    Energy capacities of methanol and hydrogen, from [(Arico2009)][Arico2009]. Capacities for lithium ion batteries are presented for comparison (*ibid*).
  </caption>
  <tr>
    <th>Fuel</th>
    <th>Energy Density<br>(Wh/L)</th>
    <th>Specific Energy<br>(Wh/kg)</th>
  </tr>
  <tr>
    <td>Methanol</td>
    <td>3228 &ndash; 3976</td>
    <td>5390 &ndash; 7122</td>
  </tr>
  <tr>
    <td>hydrogen<br>(metal hydride)</td>
    <td>1532 &ndash; 2339</td>
    <td>374 &ndash; 635</td>
  </tr>
  <tr>
    <td>hydrogen<br>(cryogenic liquid)</td>
    <td>1839 &ndash; 2317</td>
    <td>25,316 &ndash; 33,172</td>
  </tr>
  <tr>
    <td>Li-ion</td>
    <td>256 &ndash; 394</td>
    <td>86 &ndash; 147</td
  </tr>
</table>

While in portable applications both weight and volume are important considerations, reducing system volume is more important than weight; and although liquid hydrogen provides a 4.6-fold increase in gravimetric capacity, methanol has a 75.5% higher volumetric capacity than cryogenic hydrogen.

Currently, methanol is produced predominantly by steam reforming methane. However unlike other higher order alcohols, technologies exist at a sufficient technological readiness level for the commercial production of methanol from biomass.

> "While natural gas is most often used in the global economy, methanol has the distinct advantage of 'polygeneration' - whereby methanol can be made from any resource that can be converted first into synthesis gas. Through gasification, synthesis gas can be produced from anything that is or ever was a plant.  This includes biomass, agricultural and timber waste, solid municipal waste, and a number of other feedstocks."

<div align="right">
[Methanol Institute](http://www.methanol.org/methanol-basics/overview/how-is-methanol-made-.aspx "Methanol Institute"), Accessed: 12 February 2015
</div>

Thus, the use of methanol could result in the closed cycle production, distribution, and reclamation of carbon, resulting in a carbon-neutral, renewable fuel source.

For these reasons, this work will focus on the integration of direct methanol fuel cells as the power generator.

## Batteries
There are many energy storage options: lithium ion, magnesium ion, redox flow, supercapacitors. (Expand discussion on the down selection from these to lithium ion batteries.)

With volumetric energy densities between 256 and 394 Wh/L and specific energies between 86 and 147 Wh/kg [(Arico2009)][Arico2009], lithium ion batteries have energy capacities and kinetics sufficient to handle fluctuations in power demands.

The use of liquid electrolytes in lithium ion battery chemistries increases the complexity of battery design and are involved in numerous unsafe redox reactions, particularly at overcharged and undercharged conditions. Solid state lithium ion batteries do not suffer from operational limitations that plague these chemistries.

A hybrid power systems ensures the battery remain within the broad window for optimal battery performance.

For these reasons, this work will focus on integration of solid state lithium ion batteries as the power storage medium.

## Conclusion
A fuel cell-electrochemical energy storage hybrid power system is not a new concept, e.g. [(Glauchia2011)][Glauchia2011]; they have been incorporated into concept vehicles produced by several automobile manufacturers, and in May 2008, [Boeing reported][Boeing2008] on the successful test flight of the Demonstrator Airplane, which combined a proton exchange membrane fuel cell system *-- used to power the aircraft at a cruise speed of 60 mph --(drop?)* with a lightweight battery that provided additional power for takeoff. Commercial hybrid power systems have a place, but these examples show that prohibitive limitations persist in battery/hydrogen fuel cell systems, prompting our proposed move to methanol.

This project will leverage recent advancements in membrane and catalyst technology to increase the performance of direct methanol fuel cells; advance solid state lithium ion battery systems to lower battery weight, improve safety, and exploit the capacity multiplier effect of a hybrid system; and finally, advance the technological readiness level of this technology toward commercialization.

## Personnel

Dr. Branden Kappes (Lead) holds a Research Assistant Professor appointment at the Colorado School of Mines and, as VP of Technology at Process Group International (PGI), is responsible for research, development, and manufacture of their direct methanol fuel cell line. His work at the Colorado School of Mines focuses on high-throughput computational modeling of chemical and materials systems for electrochemical energy storage.

Dr. Chunmei Ban &hellip; battery system

Dr. Steven Christensen &hellip; characterization

Dr. Cristian Ciobanu &hellip; system-level modeling

Dr. Katherine Hurst &hellip; synthesis

## References
[Aric&ograve;, A., Baglio, V. & Antonucci, V. in Electrocatal. Direct Methanol Fuel Cells 1-78 (2009).][Arico2009]

[Koehler, T. Boeing makes history with flights of Fuel Cell Demonstrator Airplane, Boeing Frontiers (May 2008) 44. Accessed 12 February 2015][Boeing2008]

[Gauchia, L., Bouscayrol, a., Sanz, J., Trigui, R. & Barrade, P. Fuel cell, battery and supercapacitor hybrid system for electric vehicle: Modeling and control via energetic macroscopic representation. 2011 IEEE Veh. Power Propuls. Conf. 1–6 (2011).][Glauchia2011]

[Grove, W. R. A New Voltaic Combination. London Edinburgh Philos. Mag. J. Sci. 13, 430–431 (1838).][Grove1838]

[Grove, W. R. Voltaic Series and the Combination of Gases by Platinum. London Edinburgh Philos. Mag. J. Sci. 14, 127–130 (1839).][Grove1839]

[Mench, M. M. & Wang, C. Y. An In Situ Method for Determination of Current Distribution in PEM Fuel Cells Applied to a Direct Methanol Fuel Cell. J. Electrochem. Soc. 150, A79 (2003)][Mench2003]

[Remick, R. & Wheeler, D. Molten Carbonate and Phosphoric Acid Stationary Fuel Cells : Overview and Gap Analysis Molten Carbonate and Phosphoric Acid Stationary Fuel Cells : Overview and Gap Analysis. NREL/TP-560-49072 1–51 (2010). Accessed: 12 February 2015.][Rimick2010a]

[Tateishi, H. et al. Graphene Oxide Fuel Cell. J. Electrochem. Soc. 160, F1175–F1178 (2013).][Tateishi2013]

[Arico2009]: http://books.google.com/books?hl=en&lr=&id=xHsJJieZlHwC&oi=fnd&pg=PA1&dq=Direct+Methanol+Fuel+Cells+:+History+,+Status+and+Perspectives&ots=iDVDBBaEl5&sig=BtotK4fVYetE5w_cc2AigTz2Dnk "Aric&ograve;, A., Baglio, V. & Antonucci, V. in Electrocatal. Direct Methanol Fuel Cells 1-78 (2009)."

[Boeing2008]: http://www.boeing.com/news/frontiers/archive/2008/may/ts_sf04.pdf "Koehler, T. Boeing makes history with flights of Fuel Cell Demonstrator Airplane, Boeing Frontiers (May 2008) 44. Accessed 12 February 2015"

[Glauchia2011]: http://dx.doi.org/10.1109/VPPC.2011.6043246 "Gauchia, L., Bouscayrol, a., Sanz, J., Trigui, R. & Barrade, P. Fuel cell, battery and supercapacitor hybrid system for electric vehicle: Modeling and control via energetic macroscopic representation. 2011 IEEE Veh. Power Propuls. Conf. 1–6 (2011)."

[Grove1838]: https://archive.org/details/londonedinburghp13lond "Grove, W. R. A New Voltaic Combination. London Edinburgh Philos. Mag. J. Sci. 13, 430–431 (1838)."

[Grove1839]: https://archive.org/details/londonedinburghp143lond "Grove, W. R. Voltaic Series and the Combination of Gases by Platinum. London Edinburgh Philos. Mag. J. Sci. 14, 127–130 (1839)."

[Mench2003]: http://dx.doi.org/10.1149/1.1526108 "Mench, M. M. & Wang, C. Y. An In Situ Method for Determination of Current Distribution in PEM Fuel Cells Applied to a Direct Methanol Fuel Cell. J. Electrochem. Soc. 150, A79 (2003)"

[Rimick2010a]: http://www1.eere.energy.gov/hydrogenandfuelcells/pdfs/49072.pdf "Remick, R. & Wheeler, D. Molten Carbonate and Phosphoric Acid Stationary Fuel Cells : Overview and Gap Analysis Molten Carbonate and Phosphoric Acid Stationary Fuel Cells : Overview and Gap Analysis. NREL/TP-560-49072 1–51 (2010). Accessed: 12 February 2015."

[Tateishi2013]: http://jes.ecsdl.org/cgi/doi/10.1149/2.008311jes "Tateishi, H. et al. Graphene Oxide Fuel Cell. J. Electrochem. Soc. 160, F1175–F1178 (2013)."

# Notes

* impact -- *disruptive*
* figure
* methanol economy better than hydrogen
* incremental market introduction
* target energy density (volumetric & gravimetric)
* address $\mathrm{CO_2}$

## Task assignment
* manufacturing: PGI
* battery development/selection: Chunmei
* Stabilize Pt:Ru catalyst: Steve
* Methanol concentration/crossover (MEA): Branden

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
* $\mathrm{H_2O}$ management
* DC electronics require $V > 1~V$

### Battery
* limited energy storage capacity
* poor operating range (T, state of charge -- charge window)
