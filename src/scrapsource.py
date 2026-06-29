from bs4 import BeautifulSoup
import pandas as pd

# Mets ton code HTML entre les triple guillemets (j'ai raccourci ici pour l'exemple)
html_content = """
<table style="width:100%; margin-left:auto; margin-right:auto;" id="table-costs">
                  <tbody>
                    <tr>

                      <!--<th>Satellite</th>-->
                      <th>Project</th>
                      <th class="hidden-xs hidden-sm">Size</th>
                      <th class="hidden-xs">Organization</th>
                      <th class="hidden-xs hidden-sm">Manufactured (AIVT) by</th>
                      <th>Costs</th>
                      <th>Source</th>
                      <th class="hidden-xs">Funded primarily by</th>
                    </tr>
                    <tr>
                      <td><a href="../sat/aerocube-15.html" onclick="ga('send', 'event', 'Satellite', 'click', 'AeroCube-15');"><b>AeroCube-15</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">Aerospace Corporation</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$4.1 million for the whole program.</td>
                      <td><a href="https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=4718&amp;context=smallsat" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">US Air Force Space and Missile Systems Center</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/aistechsat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'AISTECHSAT (DANU) 2U');"><b>AISTECHSAT (DANU) 2U</b></a></td>
                      <td class="hidden-xs hidden-sm">2U</td>
                      <td class="hidden-xs">Aistech</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$230,000 for the single CubeSat platform</td>
                      <td><a href="https://gomspace.com/news/aistech-places-order-at-the-sum-of-200000-wit.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/amber.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Amber');"><b>Amber</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Horizon Technologies</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>£4.6 million for a full turn-key solution including two satellites, launches, operations and data delivery.</td>
                      <td><a href="https://horizontechnologies.eu/aac-clyde-space-wins-4-6-mgbp-order-from-horizon-technologies/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/iod-3.html" onclick="ga('send', 'event', 'Satellite', 'click', 'IOD Mission 3');"><b>IOD Mission 3</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Horizon Technologies</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$1,880,000 for four 3U IOD Mission platforms and $265,000 to upgrade this into 6U</td>
                      <td><a href="https://www.clyde.space/latest/56-clyde-space-catapults-to-more-success" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">UK Satellite Applications Catapult</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/blackcat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'BlackCAT');"><b>BlackCAT</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Pennsylvania State University (Penn State)</td>
                      <td class="hidden-xs hidden-sm">NanoAvionics</td>
                      <td>$5.8M</td>
                      <td><a href="https://www.psu.edu/news/research/story/penn-state-astrophysicist-lead-58-million-nasa-cubesat-mission/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/bro-unseenlabs.html" onclick="ga('send', 'event', 'Satellite', 'click', 'BRO');"><b>BRO</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Unseenlabs</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>43 MSEK or $4.2M for 6 satellites.</td>
                      <td><a href="https://gomspace.com/news/gomspace-signs-contract-with-unseenlabs-to-de.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/buccaneer.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Buccaneer ');"><b>Buccaneer </b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Australian Defence Science and Technology Organisation</td>
                      <td class="hidden-xs hidden-sm">Inovor</td>
                      <td>$2.5M</td>
                      <td><a href="https://www.criticalcomms.com.au/content/research/news/inovor-to-deliver-satellite-bus-for-buccaneer-project-1333916370#axzz66zQjL8U6" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Australian Defence Force</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/ctos.html" onclick="ga('send', 'event', 'Satellite', 'click', 'CTOS');"><b>CTOS</b></a></td>
                      <td class="hidden-xs hidden-sm">8U</td>
                      <td class="hidden-xs">Galaxia</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$2.5 million</td>
                      <td><a href="https://spaceq.ca/galaxia-lands-2-5m-drdc-contract-to-build-tactical-leo-satellite/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Defence Research and Development Canada (DRDC)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/catsat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'CatSat');"><b>CatSat</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">University of Arizona</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$450000 for the GomSpace 6U platform.</td>
                      <td><a href="https://gomspace.com/news/gomspace-leads-development-of-a-teaming-agreement-.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/exoterra-cubesat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Exoterra CubeSat');"><b>Exoterra CubeSat</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">Exoterra Resource</td>
                      <td class="hidden-xs hidden-sm">In-house?</td>
                      <td>$2 million from NASA Tipping Point.</td>
                      <td><a href="https://www.nasa.gov/press-release/nasa-announces-new-tipping-point-partnerships-for-moon-and-mars-technologies" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">NASA</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/cute.html" onclick="ga('send', 'event', 'Satellite', 'click', 'CUTE');"><b>CUTE</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">University of Colorado Boulder</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>The budget for developing, assembling and operating CUTE through the summer of 2024 is about $5.5 million.</td>
                      <td><a href="https://spacenews.com/cubesat-offers-template-for-future-astronomy-missions/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/daili.html" onclick="ga('send', 'event', 'Satellite', 'click', 'DAILI');"><b>DAILI</b></a></td>
                      <td class="hidden-xs hidden-sm">6U (1x6U)</td>
                      <td class="hidden-xs">Aerospace Corporation</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>Cost to completion was $3.2M. </td>
                      <td><a href="https://aerospace.org/press-release/aerospace-gets-28m-nasa-grant-study-atmosphere" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">NASA</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/aistechsat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'AISTECHSAT (DANU) 2U');"><b>AISTECHSAT (DANU) 2U</b></a></td>
                      <td class="hidden-xs hidden-sm">2U</td>
                      <td class="hidden-xs">Aistech</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$1,570,000 for additional 6 DANU platforms and for AIVT of 10 DANU CubeSats</td>
                      <td><a href="https://gomspace.com/news/gomspace-and-aistech-sign-new-agreement.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/deorbitsail.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Deorbitsail');"><b>Deorbitsail</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">EU FP7 consortium</td>
                      <td class="hidden-xs hidden-sm">SSTL</td>
                      <td>$3,200,000 for the whole project and consortium including platform and launch</td>
                      <td><a href="https://cordis.europa.eu/project/rcn/97975/reporting/en" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">EU / European Commission</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/diamond-6u.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Diamond 6U (Sky and Space Global)');"><b>Diamond 6U (Sky and Space Global)</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Sky and Space</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$5,950,000 is the order value for the first batch of 8 CubeSats</td>
                      <td><a href="https://gomspace.com/news/6u-agreement-between-gomspace-and-sky-and-spa.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/dover.html" onclick="ga('send', 'event', 'Satellite', 'click', 'DOVER');"><b>DOVER</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">RHEA Group</td>
                      <td class="hidden-xs hidden-sm">Open Cosmos</td>
                      <td>Co-funded by the UK Space Agency’s investment in the European Space Agency’s NAVISP.</td>
                      <td></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/duplex.html" onclick="ga('send', 'event', 'Satellite', 'click', 'DUPLEX');"><b>DUPLEX</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">CU Aerospace</td>
                      <td class="hidden-xs hidden-sm">NearSpace Launch</td>
                      <td>$1.7 million</td>
                      <td><a href="https://aerospace.illinois.edu/news/nasa-funds-long-standing-partners-cubesat-development?fbclid=IwAR1Fd1cpimSsh19dRQfbJpp5dSAj2M2bDkqmViQ5EYdYxYwBEzn8tMKytPo" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">NASA</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/etpack-dmm-eem.html" onclick="ga('send', 'event', 'Satellite', 'click', 'E.T.PACK DMM &amp; EEM');"><b>E.T.PACK DMM &amp; EEM</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">Universidad Carlos III de Madrid</td>
                      <td class="hidden-xs hidden-sm">?</td>
                      <td>€5.5M</td>
                      <td><a href="https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=5419&amp;context=smallsat" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">EU / European Commission</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/edison.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Edison');"><b>Edison</b></a></td>
                      <td class="hidden-xs hidden-sm">8U</td>
                      <td class="hidden-xs">Space Inventor</td>
                      <td class="hidden-xs hidden-sm">Space Inventor</td>
                      <td>$0.96M million for spacecraft, launch and operation.</td>
                      <td><a href="https://www.linkedin.com/posts/space-inventor_we-are-happy-to-announce-that-space-inventor-activity-6762415859404181505-M2qs/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)The Danish MInistry of Higher Education and Science</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/eirsat-1.html" onclick="ga('send', 'event', 'Satellite', 'click', 'EIRSAT-1');"><b>EIRSAT-1</b></a></td>
                      <td class="hidden-xs hidden-sm">2U</td>
                      <td class="hidden-xs">University College Dublin</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>€1.5 million</td>
                      <td><a href="https://europeanspaceflight.com/ireland-commit-3-3m-euros-more-to-esa-for-2024/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Irish Research CouncilESA (European Space Agency)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/wyvern-cubesats.html" onclick="ga('send', 'event', 'Satellite', 'click', 'EPICHyper');"><b>EPICHyper</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">AAC Clyde Space</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$12.1 million from the UK Space Agency together for the first and second phases.</td>
                      <td><a href="https://spacenews.com/aac-clyde-space-to-develop-cubesats-to-offer-array-of-services/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">UK Space Agency</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/et-smart-rss.html" onclick="ga('send', 'event', 'Satellite', 'click', 'ET-SMART-RSS');"><b>ET-SMART-RSS</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Ethiopian Space Science &amp; Technology Institute (ESSTI)</td>
                      <td class="hidden-xs hidden-sm">Smart Satellite</td>
                      <td>$1.5 million in total funded jointly by the Belt &amp; Road Initiative and Sunny Group.</td>
                      <td></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/facsat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'FACSAT');"><b>FACSAT</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Colombian Air Force</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$770,000</td>
                      <td><a href="https://gomspace.com/news/the-colombian-air-force-initiates-its-second-.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/faraday-1.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Faraday-1');"><b>Faraday-1</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">In-Space Missions</td>
                      <td class="hidden-xs hidden-sm">In-house?</td>
                      <td>£4.9 million for this and future validation missions.</td>
                      <td><a href="https://www.gov.uk/government/news/british-built-satellites-will-help-fight-climate-change-and-save-wildlife" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/gems-orbital-micro-systems.html" onclick="ga('send', 'event', 'Satellite', 'click', 'GEMS (Orbital Micro Systems)');"><b>GEMS (Orbital Micro Systems)</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Orbital Micro Systems</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$785,000</td>
                      <td><a href="https://investor.aac-clyde.space/en/press-releases/aac-clyde-space-wins-8-msek-order-for-commercial-satellite-75931" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">UK Space Launch Programme</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/gomx-5.html" onclick="ga('send', 'event', 'Satellite', 'click', 'GOMX-5');"><b>GOMX-5</b></a></td>
                      <td class="hidden-xs hidden-sm">8U</td>
                      <td class="hidden-xs">GomSpace</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>Over $2 million in total as of 2020.</td>
                      <td><a href="https://gomspace.com/news/esa-and-gomspace-sign-contract-for-continuati.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/hammer.html" onclick="ga('send', 'event', 'Satellite', 'click', 'HAMMER (IOD6)');"><b>HAMMER (IOD6)</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Open Cosmos</td>
                      <td class="hidden-xs hidden-sm">Open Cosmos</td>
                      <td>£3 million to support the build of the new satellite</td>
                      <td><a href="https://www.open-cosmos.com/news/open-cosmos-to-build-the-uk-pathfinder-atlantic-constellation-satellite-to-use-ai-to-improve-environmental-management" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">UK Space Agency</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/hellenic-space-dawn.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Hellenic Space Dawn');"><b>Hellenic Space Dawn</b></a></td>
                      <td class="hidden-xs hidden-sm">8U</td>
                      <td class="hidden-xs">EMTech Space</td>
                      <td class="hidden-xs hidden-sm">?</td>
                      <td>€4 million</td>
                      <td><a href="https://www.kathimerini.gr/society/562723270/erchetai-sminos-ellinikon-nanodoryforon/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/hermes.html" onclick="ga('send', 'event', 'Satellite', 'click', 'HERMES-SP');"><b>HERMES-SP</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">INAF (National Institute for Astrophysics)</td>
                      <td class="hidden-xs hidden-sm">Politecnico di Milano</td>
                      <td>$3,950,000 for the whole consortium including 6 spacecraft (HERMES-SP, HERMES-TP) with launches and operations</td>
                      <td><a href="https://cordis.europa.eu/project/rcn/218722/factsheet/en" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">EU / European CommissionItalian Space Agency (ASI)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/hyperion.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Hyperion 1');"><b>Hyperion 1</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">Inovor</td>
                      <td class="hidden-xs hidden-sm">Inovor</td>
                      <td>$3.85 million</td>
                      <td><a href="https://www.minister.defence.gov.au/minister/melissa-price/media-releases/28-million-innovation-boost-australias-defence-industry" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Australian Defence Force</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/infante.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Infante');"><b>Infante</b></a></td>
                      <td class="hidden-xs hidden-sm">16U</td>
                      <td class="hidden-xs">Tekever</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$10 million for total costs of the consortium.</td>
                      <td><a href="https://www.tekever.com/projects/infante/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">EU / European Commission</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/inspiresat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'InspireSAT');"><b>InspireSAT</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">StarSpec</td>
                      <td class="hidden-xs hidden-sm">?</td>
                      <td>$2.15 million</td>
                      <td><a href="https://spaceq.ca/starspec-12u-inspiresat-demo-satellite-launch-expected-mid-2027/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Canadian Space Agency</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/intuition-1.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Intuition-1');"><b>Intuition-1</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">KP Labs</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$1,200,000 for design, manufacturing, launch and early operations. $650,000 is for the platform.</td>
                      <td><a href="http://investor.aacmicrotec.com/pressmeddelanden/aac-microtec-wins-5-msek-launch-order-from-kp-labs-69761?page=3" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/io-1.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Io-1');"><b>Io-1</b></a></td>
                      <td class="hidden-xs hidden-sm">4U</td>
                      <td class="hidden-xs">Iota Technology</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$2.5 million for end-to-end 3-year mission.</td>
                      <td><a href="https://investor.aac-clyde.space/en/press-releases/?slug=aac-clyde-space-wins-sek-25-5-m-order-for-magquest-mission-21158" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/startical.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Startical');"><b>Startical</b></a></td>
                      <td class="hidden-xs hidden-sm">16U</td>
                      <td class="hidden-xs">Startical</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>€14.5 million for the whole project including 3 spacecraft.</td>
                      <td><a href="https://gomspace.com/news/gomspace-has-been-chosen-to-develop-advanced-.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/gems-orbital-micro-systems.html" onclick="ga('send', 'event', 'Satellite', 'click', 'GEMS (Orbital Micro Systems)');"><b>GEMS (Orbital Micro Systems)</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">Orbital Micro Systems</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$1,880,000 for four 3U IOD Mission platforms</td>
                      <td></td>
                      <td class="hidden-xs">UK Satellite Applications Catapult</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/ionsat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'IonSat');"><b>IonSat</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Ecole Polytechnique</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>Budget total estimate: 1.4 M€.</td>
                      <td><a href="https://www.polytechnique.edu/recherche/chaires/les-chaires-de-transports-mobilites-et-espace/mecenat-denseignement-espace-science-et-defis-du-spatial/centre-spatial-de-lecole-polytechnique/ionsat" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/juventas.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Juventas');"><b>Juventas</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">ESA (European Space Agency)</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$13 million to deliver spacecraft and payloads.</td>
                      <td><a href="https://spacewatch.global/2020/08/esa-and-gomspace-sign-contract-for-implementation-of-the-juventas-cubesat-in-support-of-the-hera-mission/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/kelpie.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Kelpie');"><b>Kelpie</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">AAC Clyde Space</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$5,900,000 for the manufacturing, launch and long-term operations of two CubeSats</td>
                      <td><a href="http://investor.aacmicrotec.com/pressmeddelanden/aac-microtec-to-deliver-enhanced-ais-data-exclusively-to-orb-70246" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/kepler-tars.html" onclick="ga('send', 'event', 'Satellite', 'click', 'TARS (Kepler)');"><b>TARS (Kepler)</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Kepler Communications</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$880,000 grant for the mission (actual CubeSat costs unknown)</td>
                      <td></td>
                      <td class="hidden-xs">UK Satellite Applications Catapult</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/kleos-space.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Kleos Space - Polar Vigilance Mission (KSF1)');"><b>Kleos Space - Polar Vigilance Mission (KSF1)</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Kleos Space</td>
                      <td class="hidden-xs hidden-sm">ISISpace</td>
                      <td>$2.5 million for the 4 satellite contract</td>
                      <td><a href="https://www.satellitetoday.com/launch/2020/10/23/kleos-space-selects-manufacturer-for-polar-vigilance-mission-ksf1-nanosatellite/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/kleos-space.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Kleos Scouting Mission (KSM1)');"><b>Kleos Scouting Mission (KSM1)</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Kleos Space</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$2.83 million for 4 satellites</td>
                      <td><a href="https://www.linkedin.com/feed/update/urn:li:activity:6449905862378164224/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/kss-bobcat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'KSS-BOBCAT');"><b>KSS-BOBCAT</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Kawa Space</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$1.6M</td>
                      <td><a href="https://www.satelliteevolution.com/post/aac-clyde-space-wins-sek-16-1-m-satellite-order-from-kawa-space" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/kuwaitsat-1.html" onclick="ga('send', 'event', 'Satellite', 'click', 'KuwaitSat-&#xFEFF;1');"><b>KuwaitSat-&#xFEFF;1</b></a></td>
                      <td class="hidden-xs hidden-sm">2U</td>
                      <td class="hidden-xs">Kuwait University</td>
                      <td class="hidden-xs hidden-sm">NanoAvionics</td>
                      <td>$970,000</td>
                      <td><a href="https://english.news.cn/20220916/b70417c860e144e3a13ec34aaa421b69/c.html" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Kuwait Foundation for the advancement of Sciences (KFAS)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/llited.html" onclick="ga('send', 'event', 'Satellite', 'click', 'LLITED');"><b>LLITED</b></a></td>
                      <td class="hidden-xs hidden-sm">1.5U</td>
                      <td class="hidden-xs">Aerospace Corporation</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$2,520,000 for two spacecraft and mission including launch and operations</td>
                      <td><a href="https://aerospace.org/press-release/aerospace-awarded-nasa-llited-grant" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">NASA</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/lusospace-8u.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Lusiada (LusoSpace)');"><b>Lusiada (LusoSpace)</b></a></td>
                      <td class="hidden-xs hidden-sm">8U</td>
                      <td class="hidden-xs">LusoSpace</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>AAC Clyde Space won a GBP 4.3 M order for 11 satellite kits from LusoSpace.</td>
                      <td><a href="https://www.aac-clyde.space/articles/interim-report-for-aac-clyde-space-ab-publ-january-march-2024" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/m-argo.html" onclick="ga('send', 'event', 'Satellite', 'click', 'M-ARGO');"><b>M-ARGO</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">ESA (European Space Agency)</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$450,000 for Phase-A</td>
                      <td><a href="https://gomspace.com/news/gomspace-to-design-worlds-first-stand-alone-n.aspx" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/macsat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'MACSAT');"><b>MACSAT</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">OQ Technology</td>
                      <td class="hidden-xs hidden-sm">NanoAvionics</td>
                      <td>$2.4 million</td>
                      <td><a href="https://www.oqtec.space/news/oq-techsigns-2-million-euro-contract-with-esa" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)Luxembourg</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/mantis-us.html" onclick="ga('send', 'event', 'Satellite', 'click', 'MANTIS (US)');"><b>MANTIS (US)</b></a></td>
                      <td class="hidden-xs hidden-sm">16U</td>
                      <td class="hidden-xs">University of Colorado Boulder</td>
                      <td class="hidden-xs hidden-sm">In-house?</td>
                      <td>$8.5M</td>
                      <td><a href="https://lasp.colorado.edu/missions/mantis/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/marco.html" onclick="ga('send', 'event', 'Satellite', 'click', 'MarCO');"><b>MarCO</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">NASA Jet Propulsion Laboratory</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$18,500,000 for two spacecraft and all project costs</td>
                      <td><a href="https://mars.nasa.gov/news/8408/beyond-mars-the-mini-marco-spacecraft-fall-silent/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">NASA</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/mh1.html" onclick="ga('send', 'event', 'Satellite', 'click', 'MH-1 (AEROS)');"><b>MH-1 (AEROS)</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">CEiiA</td>
                      <td class="hidden-xs hidden-sm">?</td>
                      <td>Investment of €2.8 million funded by PT2020. </td>
                      <td><a href="https://cmuportugal.org/media/mh-1-the-first-satellite-totally-developed-in-portugal-was-launched-to-space/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/mir-sat1.html" onclick="ga('send', 'event', 'Satellite', 'click', 'MIR-SAT1');"><b>MIR-SAT1</b></a></td>
                      <td class="hidden-xs hidden-sm">1U</td>
                      <td class="hidden-xs">Mauritius Research Council</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$405,00 for platform, operations, ground stations and training.</td>
                      <td><a href="http://investor.aacmicrotec.com/pressmeddelanden/aac-microtec-formalizes-collaboration-with-mauritius-researc-67858?page=4" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Mauritius Research Council</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/mobius.html" onclick="ga('send', 'event', 'Satellite', 'click', 'MOBIUS');"><b>MOBIUS</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">Galaxia</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$2.8 million</td>
                      <td><a href="https://spaceq.ca/galaxias-mobius-1-progresses-towards-june-launch/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Canadian Space Agency</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/nanomagsat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'NanoMagSat');"><b>NanoMagSat</b></a></td>
                      <td class="hidden-xs hidden-sm">16U</td>
                      <td class="hidden-xs">Open Cosmos</td>
                      <td class="hidden-xs hidden-sm">Open Cosmos</td>
                      <td>€34.6M</td>
                      <td><a href="https://www.ipgp.fr/en/news-and-agenda/news/la-mission-nanomagsat-obtient-le-feu-vert-de-lesa/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/narsscube.html" onclick="ga('send', 'event', 'Satellite', 'click', 'NARSSCube-2');"><b>NARSSCube-2</b></a></td>
                      <td class="hidden-xs hidden-sm">1U</td>
                      <td class="hidden-xs">National Authority for Remote Sensing and Space Sciences (NARSS)</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$60000</td>
                      <td><a href="http://satelliteprome.com/news/egypt-sends-cubesat-to-international-space-station/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/neptuno.html" onclick="ga('send', 'event', 'Satellite', 'click', 'NEPTUNO');"><b>NEPTUNO</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">Elecnor Deimos</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$2.8M is the total budget.</td>
                      <td><a href="https://elecnor-deimos.com/portfolio/neptuno/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ERDF (European Regional Development Fund)Self-funded</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/nslcomm-nslsat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'NSLSat');"><b>NSLSat</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">BeetleSat (NSLComm)</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$1.5 million for the &amp;U satellite, launch and operations plus a ground segment software solution.</td>
                      <td><a href="https://investor.aac-clyde.space/en/press-releases/aac-clyde-space-wins-15-msek-satellite-order-from-nslcomm-74601" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/ops-sat.html" onclick="ga('send', 'event', 'Satellite', 'click', 'OPS-SAT');"><b>OPS-SAT</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">ESA (European Space Agency)</td>
                      <td class="hidden-xs hidden-sm">Graz University of Technology</td>
                      <td>$2.66 million</td>
                      <td><a href="https://www.eurekalert.org/pub_releases/2019-12/guot-ssl121819.php" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/ops-sat-volt.html" onclick="ga('send', 'event', 'Satellite', 'click', 'OPS-SAT VOLT');"><b>OPS-SAT VOLT</b></a></td>
                      <td class="hidden-xs hidden-sm">16U</td>
                      <td class="hidden-xs">Craft Prospect</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$2.5 million</td>
                      <td><a href="https://www.aac-clyde.space/articles/interim-report-for-aac-clyde-space-ab-publ-january-march-2024" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/orca.html" onclick="ga('send', 'event', 'Satellite', 'click', 'ORCA-8');"><b>ORCA-8</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">DARPA</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$4.5 million for the program</td>
                      <td><a href="https://www.aflcmc.af.mil/News/Article-Display/Article/2034623/afrl-technology-set-for-launch-to-international-space-station/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">US Air Force</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/outernet-1u.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Outernet 1U');"><b>Outernet 1U</b></a></td>
                      <td class="hidden-xs hidden-sm">1U</td>
                      <td class="hidden-xs">Outernet</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$1,250,000 for three Outernet CubeSat platforms</td>
                      <td><a href="http://www.spacedaily.com/reports/Clyde_Space_wins_Outernet_contract_999.html" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">UK Space Agency</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/pearls.html" onclick="ga('send', 'event', 'Satellite', 'click', 'PEARLS (Sky and Space Global)');"><b>PEARLS (Sky and Space Global)</b></a></td>
                      <td class="hidden-xs hidden-sm">8U</td>
                      <td class="hidden-xs">Sky and Space</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$5,950,000 is the order value for the first batch of 8 CubeSats</td>
                      <td><a href="https://gomspace.com/news/6u-agreement-between-gomspace-and-sky-and-spa.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/phasma.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Phasma');"><b>Phasma</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">Libre Space Foundation</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>€2 million</td>
                      <td><a href="https://news.satnews.com/2023/07/20/libre-space-foundations-2-million-euros-phasma-project-with-esa-for-development-of-three-open-source-cubesats/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/pisat-poland.html" onclick="ga('send', 'event', 'Satellite', 'click', 'PIAST');"><b>PIAST</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Poland’s Armed Forces</td>
                      <td class="hidden-xs hidden-sm">Creotech</td>
                      <td>$18 million, of which about 40 percent will be allocated to Creotech Instruments to finance its share of the work.</td>
                      <td><a href="https://spacenews.com/polish-armed-forces-enlist-industry-consortium-for-imaging-nanosatellites/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Poland's National Center for Research and Development</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/pixl-1.html" onclick="ga('send', 'event', 'Satellite', 'click', 'PIXL-1');"><b>PIXL-1</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">DLR (German Aerospace Center)</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$560,000 for the single CubeSat platform</td>
                      <td><a href="https://gomspace.com/news/gomspace-closes-order-for-a-nano-satellite-pl.aspx" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">DLR (German Aerospace Center)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/polsir.html" onclick="ga('send', 'event', 'Satellite', 'click', 'PolSIR');"><b>PolSIR</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">Vanderbilt University</td>
                      <td class="hidden-xs hidden-sm">Blue Canyon</td>
                      <td>Up to $37 million, not including launch costs.</td>
                      <td><a href="https://news.vanderbilt.edu/2023/05/25/vanderbilt-universitys-ralf-bennartz-to-lead-nasa-mission-to-study-ice-clouds/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/lusospace-3u.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Lusiada (LusoSpace)');"><b>Lusiada (LusoSpace)</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">LusoSpace</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>AAC Clyde Space won a GBP 4.3 M order for 11 satellite kits from LusoSpace.</td>
                      <td><a href="https://www.aac-clyde.space/articles/interim-report-for-aac-clyde-space-ab-publ-january-march-2024" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/prefire.html" onclick="ga('send', 'event', 'Satellite', 'click', 'PREFIRE');"><b>PREFIRE</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">University of Wisconsin</td>
                      <td class="hidden-xs hidden-sm">?</td>
                      <td>$33 million</td>
                      <td><a href="https://spacenews.com/rocket-lab-to-launch-pair-of-nasa-earth-science-cubesats/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/race-esa.html" onclick="ga('send', 'event', 'Satellite', 'click', 'RACE (ESA)');"><b>RACE (ESA)</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">ESA (European Space Agency)</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$450,000 for the first phase A of two CubeSats for the larger consortium</td>
                      <td><a href="https://gomspace.com/news/gomspace-signs-contract-with-the-european-spa.aspx" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/eps-maccs.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SCOUT-1 (EPS-MACCS)');"><b>SCOUT-1 (EPS-MACCS)</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">GomSpace</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>Contract value is EUR 24,000,000. GomSpace revenue impact is EUR 10,000,000, whereof direct GomSpace revenue share will be EUR 7,000,000.</td>
                      <td><a href="https://gomspace.com/news/esa-and-gomspace-sign-contract-to-implement-e.aspx" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/seahawk.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SeaHawk');"><b>SeaHawk</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">University of North Carolina Wilmington</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$1,680,000 for two CubeSat platforms</td>
                      <td><a href="http://www.satnews.com/story.php?number=972377587 " style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Gordon and Betty Moore Foundation</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/seam.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SEAM');"><b>SEAM</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">Royal Institute of Technology (KTH)</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>$3,000,000 for the whole project and consortium including platform and launch</td>
                      <td><a href="https://cordis.europa.eu/project/rcn/188846/factsheet/en" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">EU / European Commission</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/soar.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SOAR');"><b>SOAR</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">University of Manchester</td>
                      <td class="hidden-xs hidden-sm">GomSpace</td>
                      <td>€5.7 million</td>
                      <td><a href="https://discoverer.space/soar-satellite-for-orbital-aerodynamics-research/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">EU / European Commission</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/spirit.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SpIRIT');"><b>SpIRIT</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">University of Melbourne</td>
                      <td class="hidden-xs hidden-sm">Inovor</td>
                      <td>AU$7 million.</td>
                      <td><a href="https://www.space.gov.au/australian-spirit-launches-to-space" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Australian Space Agency</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/sprite.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SPRITE');"><b>SPRITE</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">University of Colorado Boulder</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$4 million</td>
                      <td><a href="https://spacenews.com/cubesat-offers-template-for-future-astronomy-missions/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/sroc.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SROC');"><b>SROC</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">Politecnico di Torino</td>
                      <td class="hidden-xs hidden-sm">Terran Orbital</td>
                      <td>$4.7 million</td>
                      <td><a href="https://terranorbital.com/terran-orbital-awarded-4-7-million-contract-by-european-space-agency/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/sulis.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SULIS');"><b>SULIS</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">Northumbria University</td>
                      <td class="hidden-xs hidden-sm">?</td>
                      <td>$105 million for the whole consortium</td>
                      <td><a href="https://sulis.space/management-structure/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">UK Space Agency</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/sunrise.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SunRISE');"><b>SunRISE</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">NASA Jet Propulsion Laboratory</td>
                      <td class="hidden-xs hidden-sm">Utah State University Space Dynamics Laboratory</td>
                      <td>$62.6 million to design, build, and launch the SunRISE mission.</td>
                      <td><a href="https://www.nasaspaceflight.com/2020/03/sunrise-mission-study-giant-solar-particle-storms/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/swarm-ex.html" onclick="ga('send', 'event', 'Satellite', 'click', 'SWARM-EX');"><b>SWARM-EX</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">Olin College</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$4 million</td>
                      <td><a href="https://digitalcommons.usu.edu/smallsat/2022/all2022/96/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">US National Science Foundation (NSF)</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/tempest-d.html" onclick="ga('send', 'event', 'Satellite', 'click', 'TEMPEST-D');"><b>TEMPEST-D</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Colorado State University</td>
                      <td class="hidden-xs hidden-sm">Blue Canyon</td>
                      <td>$8.2 million</td>
                      <td><a href="http://www.spacedaily.com/reports/Small_nimble_CSU_satellite_has_surpassed_a_year_in_space_999.html" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/tiger-2.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Tiger-2');"><b>Tiger-2</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">OQ Technology</td>
                      <td class="hidden-xs hidden-sm">NanoAvionics</td>
                      <td>$2.4 million</td>
                      <td><a href="https://www.oqtec.space/news/oq-techsigns-2-million-euro-contract-with-esa" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)Luxembourg</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/tiger-oqtechnology.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Tiger-4');"><b>Tiger-4</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">OQ Technology</td>
                      <td class="hidden-xs hidden-sm">NanoAvionics</td>
                      <td>$2.4 million</td>
                      <td><a href="https://www.oqtec.space/news/oq-techsigns-2-million-euro-contract-with-esa" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)Luxembourg</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/tiger-oqtechnology.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Tiger-7');"><b>Tiger-7</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">OQ Technology</td>
                      <td class="hidden-xs hidden-sm">NanoAvionics</td>
                      <td>$2.4 million</td>
                      <td><a href="https://www.oqtec.space/news/oq-techsigns-2-million-euro-contract-with-esa" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)Luxembourg</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/tiger-oqtechnology.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Tiger-8');"><b>Tiger-8</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">OQ Technology</td>
                      <td class="hidden-xs hidden-sm">NanoAvionics</td>
                      <td>$2.4 million</td>
                      <td><a href="https://www.oqtec.space/news/oq-techsigns-2-million-euro-contract-with-esa" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">ESA (European Space Agency)Luxembourg</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/ukube-1.html" onclick="ga('send', 'event', 'Satellite', 'click', 'UKube-1');"><b>UKube-1</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">UK Space Agency</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$1,000,000 for CubeSat platform and ground segment</td>
                      <td><a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/350503/National_Space_Programmes_2014_to_2015.pdf" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">UK Space Agency</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/vpm.html" onclick="ga('send', 'event', 'Satellite', 'click', 'VPM');"><b>VPM</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">Air Force Research Laboratory (AFRL)</td>
                      <td class="hidden-xs hidden-sm">In-house</td>
                      <td>$4.5 million for the program</td>
                      <td><a href="https://www.aflcmc.af.mil/News/Article-Display/Article/2034623/afrl-technology-set-for-launch-to-international-space-station/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">US Air Force</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/windcube.html" onclick="ga('send', 'event', 'Satellite', 'click', 'WindCube');"><b>WindCube</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">National Center for Atmospheric Research (NCAR)</td>
                      <td class="hidden-xs hidden-sm">In-house?</td>
                      <td>$6.5 million</td>
                      <td><a href="https://digitalcommons.usu.edu/smallsat/2022/all2022/62/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">NASA Science Mission Directorate Heliophysics Division</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/xspancion.html" onclick="ga('send', 'event', 'Satellite', 'click', 'xSPANCION');"><b>xSPANCION</b></a></td>
                      <td class="hidden-xs hidden-sm">6U</td>
                      <td class="hidden-xs">AAC Clyde Space</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$12.1 million from the UK Space Agency together for the first and second phases.</td>
                      <td><a href="https://spacenews.com/aac-clyde-space-to-develop-cubesats-to-offer-array-of-services/" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">UK Space Agency</td>
                    </tr>
                    <tr>
                      <td><a href="../sat/xvi.html" onclick="ga('send', 'event', 'Satellite', 'click', 'XVI');"><b>XVI</b></a></td>
                      <td class="hidden-xs hidden-sm">12U</td>
                      <td class="hidden-xs">Viasat</td>
                      <td class="hidden-xs hidden-sm">Blue Canyon</td>
                      <td>$10 million for the whole project.</td>
                      <td><a href="https://spacenews.com/viasat-selected-to-develop-military-link-16-communications-satellite-in-low-earth-orbit/" style="font-size:14px">Link</a></td>
                      <td></td>
                    </tr>
                    <tr>
                      <td><a href="../sat/ymir.html" onclick="ga('send', 'event', 'Satellite', 'click', 'Ymir');"><b>Ymir</b></a></td>
                      <td class="hidden-xs hidden-sm">3U</td>
                      <td class="hidden-xs">AOS (AAC Clyde Space, Saab, Orbcomm)</td>
                      <td class="hidden-xs hidden-sm">AAC Clyde Space</td>
                      <td>$1.94 million</td>
                      <td><a href="https://investor.aac-clyde.space/en/press-releases/aac-clyde-space-saab-and-orbcomm-to-bring-the-next-generatio-79059" style="font-size:14px">Link</a></td>
                      <td class="hidden-xs">Swedish Transport Administration</td>
                    </tr>
                  </tbody>
                </table>
"""

# Initialiser BeautifulSoup pour parser le HTML
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', {'id': 'table-costs'})

# 1. Extraire les titres des colonnes (les <th>)
header_row = table.find('tr')
headers = [th.text.strip() for th in header_row.find_all('th')]

# Ajouter dynamiquement notre nouvelle colonne pour le lien du projet
headers.insert(1, "Project Link") 
headers.insert(0, "id") 

data = []

# 2. Parcourir toutes les lignes de données (on saute la première ligne d'en-tête [1:])
for i, row in enumerate(table.find_all('tr')[1:]):
    cols = row.find_all('td')
    
    if cols: # S'assurer que la ligne n'est pas vide
        row_data = []
        row_data.append(i + 1)  # Ajouter l'ID de la ligne
        
        # --- Colonne 1 : Projet ---
        project_td = cols[0]
        project_name = project_td.text.strip()
        
        # Extraire le lien (href) de la balise <a>
        a_tag = project_td.find('a')
        project_link = a_tag['href'] if a_tag else ""
        
        # On ajoute le nom ET le lien au tableau
        row_data.append(project_name)
        row_data.append(project_link)
        
        # --- Autres colonnes ---
        for col in cols[1:]:
            # Astuce bonus : Si la colonne contient un lien appelé "Link" (comme dans la colonne 'Source'),
            # on récupère directement son URL au lieu du mot inutile "Link".
            col_a = col.find('a')
            if col_a and col.text.strip() == "Link":
                row_data.append(col_a['href'])
            else:
                row_data.append(col.text.strip())
                
        # Ajouter la ligne complète à nos données
        data.append(row_data)

# 3. Créer un DataFrame Pandas et l'exporter en CSV
df = pd.DataFrame(data, columns=headers)

# Exporter en fichier CSV (séparateur virgule)
df.to_csv("extraction_satellites.csv", index=False, encoding='utf-8-sig')

print("Extraction terminée ! Le fichier 'extraction_satellites.csv' a été créé.")