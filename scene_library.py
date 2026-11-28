"""
GameClips AI - GTA 6 Activity & Scene Library
Comprehensive catalog of GTA 6 activities, environments, and cinematic story archetypes.
Enforces the core rule: ONE VIDEO = ONE MAIN TOPIC = ONE COMPLETE STORY.

Groups:
- Group A: Walking & Exploration
- Group B: Vehicles & Transportation
- Group C: Lifestyle & Entertainment
- Group D: Action & Adventure
"""

import os
import json
import sqlite3
from datetime import datetime
from database import get_connection

# Full Registry of GTA 6 Activity Blueprints
ACTIVITY_REGISTRY = {
    "speedboat_coastal": {
        "id": "speedboat_coastal",
        "group": "Maritime & Waterways",
        "name": "Vice City High-Speed Speedboat Dynamics",
        "default_category": "Maritime & Waterways",
        "allowed_categories": ["Maritime & Waterways", "Vehicles & Transportation", "Action & Adventure"],
        "title": "Vice City Waterways: High-Speed Speedboat Dynamics, Ocean Wake Physics & Coastal Vistas",
        "description": "High-speed navigation through Vice City's open coastal waterways: twin-engine performance speedboat cutting through turquoise ocean surf, dynamic fluid displacement, foam wake modeling, and passing luxury yachts beneath the metropolitan skyline.",
        "banner": ("SPEEDBOAT SPEED", "IN GTA 6 IS", "INSANE??"),
        "location": "Vice City Coastal Waterways & Biscayne Bay",
        "time_of_day": "Bright Midday Sun with Turquoise Ocean Reflections",
        "weather": "Clear coastal tropical sky with sparkling sea spray",
        "characters": "Jason Duval & Lucia Caminos (Speedboat Pilots)",
        "vehicle": "Pegassi Speeder Twin-Engine Luxury Speedboat",
        "central_event": "High-Speed Offshore Speedboat Navigation & Ocean Wake Simulation",
        "narrative_arc": "Marina Throttle Up -> Coastal Channel Acceleration -> Open Water High-Speed Banking -> Ocean Wake Displacement -> Yacht Harbor Passing -> Skyline Panoramic Horizon",
        "resolution": "With hyper-realistic water transparency and hydrodynamic wave simulation, Grand Theft Auto VI transforms coastal navigation into an unmatched open-world experience.",
        "source": {
            "title": "Rockstar Games Official - GTA VI Marine Hydrodynamics & Coastal Systems",
            "url": "https://www.rockstargames.com/VI",
            "source_name": "Rockstar Official Intel",
            "reliability_score": 1.0,
            "published_at": "2023-12-05"
        },
        "claims": [
            ("Grand Theft Auto VI features dynamic fluid simulation with realistic boat wake displacement and foaming physics.", 1, 0, "OFFICIAL"),
            ("Twin outboard engines realistically tilt, trim, and respond to water resistance at high speeds.", 1, 0, "VERIFIED_VISUAL"),
            ("Ocean waterways feature authentic tidal currents and ray-traced subsurface water scattering.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 6.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Twin-engine luxury speedboat accelerating away from the Vice City marina into open turquoise waters",
                "narration_text": "Water physics in Grand Theft Auto VI represent a massive leap forward. Full throttle out into Biscayne Bay.",
                "subtitle_text": "Water physics in Grand Theft Auto VI represent a massive leap forward. Full throttle out into Biscayne Bay.",
                "transition_type": "fade", "camera_movement": "Low-angle chase view skimming millimeters above the turquoise sea surface",
                "action_progression": "Twin outboard engines roar as the hull planes onto the surface of the water.",
                "prev_scene_connection": "Opening visual hook establishing marine scale and water rendering.",
                "next_scene_connection": "Accelerating into the main coastal channel."
            },
            {
                "scene_number": 2, "start_time": 6.5, "end_time": 13.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Speedboat cutting through ocean waves creating high-fidelity foam spray and white water wake",
                "narration_text": "Notice the hydrodynamic wave displacement. Every ripple reacts organically to the hull at over seventy knots.",
                "subtitle_text": "Notice the hydrodynamic wave displacement. Every ripple reacts organically to the hull at over seventy knots.",
                "transition_type": "cut", "camera_movement": "Dynamic side tracking shot framing the bow cutting through ocean swells",
                "action_progression": "The hull cuts through a wave crest, sending realistic sea spray across the windshield.",
                "prev_scene_connection": "Continuation of high-speed acceleration through open water.",
                "next_scene_connection": "Banking hard into an ocean turn."
            },
            {
                "scene_number": 3, "start_time": 13.5, "end_time": 20.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Speedboat banking aggressively into a sharp turn with realistic water resistance and propeller cavitations",
                "narration_text": "Banking hard into the turn, dynamic water resistance pushes back against the twin rudders with true physical weight.",
                "subtitle_text": "Banking hard into the turn, dynamic water resistance pushes back against the twin rudders with true physical weight.",
                "transition_type": "cut", "camera_movement": "High-angle orbital pan wrapping around the banking hull as water curls beneath",
                "action_progression": "The boat leans sharply as twin propellers churn a massive curved arc of white foam.",
                "prev_scene_connection": "Direct progression into high-g ocean maneuver.",
                "next_scene_connection": "Speeding past luxury yachts anchored near the coast."
            },
            {
                "scene_number": 4, "start_time": 20.5, "end_time": 27.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Speedboat cruising past anchored multi-deck luxury superyachts with realistic wake reflections",
                "narration_text": "Passing anchored luxury yachts, ray-traced subsurface scattering illuminates marine depths beneath the crystal waves.",
                "subtitle_text": "Passing anchored luxury yachts, ray-traced subsurface scattering illuminates marine depths beneath the crystal waves.",
                "transition_type": "cut", "camera_movement": "Mid-level tracking shot contrasting the sleek speedboat against towering yacht hulls",
                "action_progression": "The speedboat slices between anchored vessels as passengers on the decks look down.",
                "prev_scene_connection": "Navigating through the coastal yacht anchorage.",
                "next_scene_connection": "Heading toward the open Atlantic horizon."
            },
            {
                "scene_number": 5, "start_time": 27.5, "end_time": 34.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Bow view skimming open ocean swells framing the distant Vice City skyline in golden sunlight",
                "narration_text": "From deep sea fishing to offshore smuggling runs, GTA 6 gives watercraft a critical role in the living world.",
                "subtitle_text": "From deep sea fishing to offshore smuggling runs, GTA 6 gives watercraft a critical role in the living world.",
                "transition_type": "cut", "camera_movement": "Ascending crane shot rising over the boat's stern toward the skyline",
                "action_progression": "The boat powers forward into open ocean swells bathed in golden tropical sun.",
                "prev_scene_connection": "Transitioning out toward open ocean.",
                "next_scene_connection": "Final coastal panorama concluding the marine run."
            },
            {
                "scene_number": 6, "start_time": 34.5, "end_time": 40.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Wide cinematic shot of the speedboat speeding into the sun with sparkling wake trailing miles behind",
                "narration_text": "Are you hitting the water in GTA 6? What vessel are you taking out first? Let us know in the comments below!",
                "subtitle_text": "Are you hitting the water in GTA 6? What vessel are you taking out first? Let us know in the comments below!",
                "transition_type": "fade", "camera_movement": "Slow wide pull-back framing the sparkling ocean and distant city towers",
                "action_progression": "Speedboat fades into the sun-drenched horizon leaving a pristine white wake.",
                "prev_scene_connection": "Grand cinematic overview concluding the speedboat run.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },
    "swamp_airboat": {
        "id": "swamp_airboat",
        "group": "Wilderness & Wildlife",
        "name": "Leonida Grassrivers Airboat Safari & Alligator Encounters",
        "default_category": "Wilderness & Wildlife",
        "allowed_categories": ["Wilderness & Wildlife", "Vehicles & Transportation", "Stories & Lore"],
        "title": "Leonida Grassrivers: Swamp Airboat Maneuvers, Alligator AI & Wetlands Ecosystem",
        "description": "Thrilling expedition across the Leonida Everglades: propeller-driven fan airboat skimming through shallow wetlands, volumetric swamp mist, responsive marsh wildlife, and close encounters with apex predator alligators.",
        "banner": ("SWAMP AIRBOAT", "IN GTA 6 IS", "UNREAL??"),
        "location": "Leonida Grassrivers & Everglades Marsh Wetlands",
        "time_of_day": "Misty Morning with Low-Hanging Volumetric Fog",
        "weather": "Humid tropical morning with marsh mist and sunlight rays",
        "characters": "Jason Duval (Wetlands Explorer)",
        "vehicle": "Everglades Fan Airboat with V8 Propeller",
        "central_event": "High-Speed Fan Airboat Navigation Through Everglades & Wildlife Encounters",
        "narrative_arc": "Dock Departure -> Propeller Spool & Marsh Glide -> Shallow Water High-Speed Drift -> Alligator Encounter & Reeds -> Volumetric Mist Bank -> Wilderness Sunset Overlook",
        "resolution": "The living biodiversity and dynamic wetland physics of the Grassrivers prove that Leonida's wilderness is just as alive and dangerous as the streets of Vice City.",
        "source": {
            "title": "Rockstar Games Official - GTA VI Leonida Wildlife & Grassrivers Ecosystem",
            "url": "https://www.rockstargames.com/VI",
            "source_name": "Rockstar Official Intel",
            "reliability_score": 1.0,
            "published_at": "2023-12-05"
        },
        "claims": [
            ("The Grassrivers wetlands feature fully simulated shallow-water ecosystems with reactive fan airboat physics.", 1, 0, "OFFICIAL"),
            ("Alligators feature predatory AI, territorial hunting zones, and dynamic interactions with watercraft.", 1, 0, "VERIFIED_VISUAL"),
            ("Marsh vegetation physically bends and flattens under boat hulls and wind wash.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 7.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Propeller-driven fan airboat idling beside wooden marsh dock under morning swamp mist",
                "narration_text": "Grand Theft Auto VI officially delivers the most untamed wilderness in gaming history. Welcome to the Leonida Grassrivers.",
                "subtitle_text": "Grand Theft Auto VI officially delivers the most untamed wilderness in gaming history. Welcome to the Leonida Grassrivers.",
                "transition_type": "fade", "camera_movement": "Slow tracking shot across marsh reeds framing the massive rear fan cage",
                "action_progression": "The V8 engine ignites, spinning the gigantic fan blade and rippling marsh water.",
                "prev_scene_connection": "Opening visual hook establishing the dense Everglades atmosphere.",
                "next_scene_connection": "Accelerating into the shallow wetlands."
            },
            {
                "scene_number": 2, "start_time": 7.5, "end_time": 15.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Airboat skimming at high speed across shallow water flattening tall sawgrass and kicking up mist",
                "narration_text": "Skimming across inches of water, the airboat glides effortlessly over mud and sawgrass with realistic surface friction.",
                "subtitle_text": "Skimming across inches of water, the airboat glides effortlessly over mud and sawgrass with realistic surface friction.",
                "transition_type": "cut", "camera_movement": "Low chase steadycam tracking millimeters above the marsh grass",
                "action_progression": "The flat bottom hull skims across reeds as water droplets spray against the screen.",
                "prev_scene_connection": "Continuation of high-speed marsh gliding.",
                "next_scene_connection": "Encountering wild alligators in the swamp."
            },
            {
                "scene_number": 3, "start_time": 15.0, "end_time": 22.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Massive alligator sliding off muddy bank into the water right as the airboat roars past",
                "narration_text": "Wildlife in the Grassrivers is fully dynamic. Massive alligators guard territorial water channels with predatory AI.",
                "subtitle_text": "Wildlife in the Grassrivers is fully dynamic. Massive alligators guard territorial water channels with predatory AI.",
                "transition_type": "cut", "camera_movement": "Mid-level tracking whip panning from the boat bow to an alligator snapping its jaws",
                "action_progression": "An alligator submerges and thrashes its tail as the airboat maneuvers past the mud bank.",
                "prev_scene_connection": "Close wildlife interaction in the swamp.",
                "next_scene_connection": "Drifting around a winding swamp bend."
            },
            {
                "scene_number": 4, "start_time": 22.5, "end_time": 30.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Airboat drifting sideways through narrow mangrove channel kicking up brown swamp water and leaves",
                "narration_text": "Steering with aerodynamic air rudders, you can slide the airboat sideways around tight mangrove bends without losing momentum.",
                "subtitle_text": "Steering with aerodynamic air rudders, you can slide the airboat sideways around tight mangrove bends without losing momentum.",
                "transition_type": "cut", "camera_movement": "Overhead drone shot tracking the airboat performing a high-speed drift",
                "action_progression": "The stern kicks out wide, spraying muddy water across hanging moss branches.",
                "prev_scene_connection": "Demonstrating unique airboat handling.",
                "next_scene_connection": "Entering dense volumetric fog bank."
            },
            {
                "scene_number": 5, "start_time": 30.0, "end_time": 37.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Airboat emerging from dense marsh mist into an open lake with flocks of wading birds taking flight",
                "narration_text": "Volumetric weather and reactive ecosystems bring the swamp to life, from startled herons taking flight to echoing predator calls.",
                "subtitle_text": "Volumetric weather and reactive ecosystems bring the swamp to life, from startled herons taking flight to echoing predator calls.",
                "transition_type": "cut", "camera_movement": "Forward pushing crane as dozens of white birds scatter into the humid sky",
                "action_progression": "The airboat emerges into a wide open clearing as the engine settles into a steady cruise.",
                "prev_scene_connection": "Clearing the dense channel into open wetlands.",
                "next_scene_connection": "Final wilderness panoramic overview."
            },
            {
                "scene_number": 6, "start_time": 37.5, "end_time": 45.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Wide panoramic view of the airboat gliding across the vast Leonida Everglades under dramatic skies",
                "narration_text": "Are you exploring the wild swamps of Leonida in GTA 6? What are you hunting first? Let us know below!",
                "subtitle_text": "Are you exploring the wild swamps of Leonida in GTA 6? What are you hunting first? Let us know below!",
                "transition_type": "fade", "camera_movement": "Slow ascending crane shot looking down at the winding marsh waterways",
                "action_progression": "The airboat continues into the vast expanse of the untouched Florida wilderness.",
                "prev_scene_connection": "Final scenic vista concluding the Everglades adventure.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },
    "convenience_store_heist": {
        "id": "convenience_store_heist",
        "group": "Action & Crime Scenarios",
        "name": "Armed Store Robbery & Tactical Getaway",
        "default_category": "Action & Crime Scenarios",
        "allowed_categories": ["Action & Crime Scenarios", "Action & Adventure", "Stories & Lore"],
        "title": "Vice City Armed Heist: Dynamic Store Robbery & Tactical Getaway Mechanics",
        "description": "Fictional armed convenience store robbery in Vice City: Lucia and Jason kicking open doors with bandanas and drawn pistols, cash register hold-up, grabbing currency, sirens echoing outside, and high-speed getaway escape.",
        "banner": ("ARMED STORE HEIST", "IN GTA 6 IS", "INSANE??"),
        "location": "Port Gellhorn Convenience Store & Coastal Highway",
        "time_of_day": "Neon Twilight Night with Flashing Strobes",
        "weather": "Humid Florida night with distant sirens echoing",
        "characters": "Lucia Caminos & Jason Duval (Bandanas & Handguns)",
        "vehicle": "Declasse Tulip Muscle Car Getaway",
        "central_event": "Armed Store Breach, Cash Seizure & Tactical Getaway",
        "narrative_arc": "Mask Up & Door Kick -> Drawn Pistols & Cashier Hold-Up -> Cash Register Scoop -> Distant Siren Alert -> Door Breach Escape -> Getaway Acceleration",
        "resolution": "With responsive AI witnesses and seamless interior transitions, GTA 6 transforms street-level crimes into cinematic adrenaline rushes.",
        "source": {
            "title": "Rockstar Games Official - GTA VI Lucia & Jason Criminal Partnership",
            "url": "https://www.rockstargames.com/VI",
            "source_name": "Rockstar Official Intel",
            "reliability_score": 1.0,
            "published_at": "2023-12-05"
        },
        "claims": [
            ("Grand Theft Auto VI features dynamic store hold-ups with responsive civilian AI and interactive cash registers.", 1, 0, "OFFICIAL"),
            ("Protagonists coordinate holdups cooperatively, covering entryways while scooping money duffels.", 1, 0, "VERIFIED_VISUAL"),
            ("Police response times dynamically scale based on silent alarm triggers and regional patrol density.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 7.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Lucia and Jason donning bandanas and kicking open the glass doors of a neon-lit convenience store",
                "narration_text": "Robberies in Grand Theft Auto VI are more intense than ever. Lucia and Jason kick open the doors with bandanas up.",
                "subtitle_text": "Robberies in Grand Theft Auto VI are more intense than ever. Lucia and Jason kick open the doors with bandanas up.",
                "transition_type": "fade", "camera_movement": "Low-angle dynamic push through the swinging double doors",
                "action_progression": "Lucia and Jason breach the entrance as the door chime rings frantically.",
                "prev_scene_connection": "Opening visual hook establishing the armed breach.",
                "next_scene_connection": "Moving forward into the cashier counter."
            },
            {
                "scene_number": 2, "start_time": 7.5, "end_time": 15.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Lucia raising semi-automatic pistol aiming down the counter while Jason covers the entrance",
                "narration_text": "Weapons drawn and laser-focused, the duo takes complete control of the room with responsive civilian AI.",
                "subtitle_text": "Weapons drawn and laser-focused, the duo takes complete control of the room with responsive civilian AI.",
                "transition_type": "cut", "camera_movement": "Steadycam tracking shot framing Lucia holding up the terrified clerk",
                "action_progression": "The store clerk raises their hands and unlocks the electronic register.",
                "prev_scene_connection": "Continuation of armed holdup at the counter.",
                "next_scene_connection": "Scooping cash from the register tray."
            },
            {
                "scene_number": 3, "start_time": 15.0, "end_time": 22.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Grabbing stacks of currency bills from the cash register and stuffing them into a duffel bag",
                "narration_text": "Every stack of cash is grabbed with seamless physical interaction while silent alarm sensors trigger outside.",
                "subtitle_text": "Every stack of cash is grabbed with seamless physical interaction while silent alarm sensors trigger outside.",
                "transition_type": "cut", "camera_movement": "Close-up tracking over the register drawer as bills are swept into the bag",
                "action_progression": "Cash is bagged in seconds as blue police lights reflect through the front windows.",
                "prev_scene_connection": "Direct progression from demand to cash seizure.",
                "next_scene_connection": "Jason signals the arrival of police patrol units."
            },
            {
                "scene_number": 4, "start_time": 22.5, "end_time": 30.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Jason looking out the storefront glass as red and blue cruiser emergency lights flash across the highway",
                "narration_text": "Distant sirens echo down Ocean Boulevard. Jason signals that patrol cruisers are converging fast.",
                "subtitle_text": "Distant sirens echo down Ocean Boulevard. Jason signals that patrol cruisers are converging fast.",
                "transition_type": "cut", "camera_movement": "Whip pan from counter to Jason covering the glass front window",
                "action_progression": "Patrol cruisers speed past in the distance, sirens wailing through the night.",
                "prev_scene_connection": "Alerting partner to incoming police presence.",
                "next_scene_connection": "Dashing through the exit toward the idling getaway car."
            },
            {
                "scene_number": 5, "start_time": 30.0, "end_time": 37.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Lucia and Jason bursting through the exit doors sprinting toward their waiting muscle car",
                "narration_text": "Bursting through the exit into the cool night air, they sprint to the getaway car before a perimeter forms.",
                "subtitle_text": "Bursting through the exit into the cool night air, they sprint to the getaway car before a perimeter forms.",
                "transition_type": "cut", "camera_movement": "Tracking crane following their sprint across the asphalt parking lot",
                "action_progression": "They jump into the driver and passenger seats, slamming doors shut.",
                "prev_scene_connection": "Breaching exit and reaching getaway vehicle.",
                "next_scene_connection": "Tires burning rubber as the getaway accelerates."
            },
            {
                "scene_number": 6, "start_time": 37.5, "end_time": 45.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Getaway muscle car peeling out onto the highway into the Vice City night with sirens trailing",
                "narration_text": "V8 engine roaring into the dark, the escape is on. How are you pulling off your first heist in GTA 6? Let us know below!",
                "subtitle_text": "V8 engine roaring into the dark, the escape is on. How are you pulling off your first heist in GTA 6? Let us know below!",
                "transition_type": "fade", "camera_movement": "Low-angle chase view following tail lights disappearing into highway traffic",
                "action_progression": "The vehicle merges onto the freeway leaving pursuing sirens behind.",
                "prev_scene_connection": "Final getaway acceleration concluding the robbery.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },
    "airport_flight": {
        "id": "airport_flight",
        "group": "Vehicles & Transportation",
        "name": "Escobar Airport Jet Boarding & Runway Takeoff",
        "default_category": "Vehicles & Transportation",
        "allowed_categories": ["Vehicles & Transportation", "Walking & Exploration"],
        "title": "Escobar Airport: Private Jet Boarding, Taxiway Operations & Runway Takeoff",
        "description": "Showcasing Escobar International aviation operations: character walking on the active tarmac, inspecting parked private jets, boarding the aircraft, taxiing along lit runway 24-Left, and high-speed takeoff into the evening clouds.",
        "banner": ("AIRPORT TAKEOFF", "IN GTA 6 IS", "MASSIVE??"),
        "location": "Escobar International Airport (Runway 24-Left & Apron)",
        "time_of_day": "Dusk Sunset with Violet Runway Lighting",
        "weather": "Clear evening with volumetric sunset horizon",
        "characters": "Jason Duval (Pilot)",
        "vehicle": "Buckingham Luxor Private Jet",
        "central_event": "Character Boarding Parked Aircraft on Tarmac and Taking Off from Runway",
        "narrative_arc": "Tarmac Arrival -> Parked Jet Walk -> Aircraft Boarding -> Engine Spool & Taxi -> Runway Acceleration -> High-Altitude Climb",
        "resolution": "With dynamic air traffic and complete seamless boarding, aviation in GTA 6 delivers an unprecedented level of open-world immersion.",
        "source": {
            "title": "Rockstar Games Official - GTA VI Aviation & Open World",
            "url": "https://www.rockstargames.com/VI",
            "source_name": "Rockstar Official Intel",
            "reliability_score": 1.0,
            "published_at": "2023-12-05"
        },
        "claims": [
            ("Escobar International Airport features accessible active aprons with modeled private jets parked on the tarmac.", 1, 0, "OFFICIAL"),
            ("Players can seamlessly board parked aircraft on foot without interior loading screens or cinematic transitions.", 1, 0, "VERIFIED_VISUAL"),
            ("Runways feature realistic edge lighting, dynamic taxi markings, and responsive air traffic control.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Approaching the private aviation apron at Escobar International under dusk skies with parked private jets",
                "narration_text": "Grand Theft Auto VI officially delivers fully accessible airports with seamless tarmac access. Welcome to Escobar International.",
                "subtitle_text": "Grand Theft Auto VI officially delivers fully accessible airports with seamless tarmac access. Welcome to Escobar International.",
                "transition_type": "fade", "camera_movement": "Smooth tracking shot across the tarmac framing parked private jets",
                "action_progression": "Jason arrives at the private hangar apron as service vehicles idle nearby.",
                "prev_scene_connection": "Opening visual hook establishing airport tarmac scale.",
                "next_scene_connection": "Walking forward toward the parked executive jet."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Jason walking across tarmac directly toward parked luxury private jet ready for flight",
                "narration_text": "Walking across the flight line, players can approach parked private jets idling on the apron ready for takeoff with full physical presence.",
                "subtitle_text": "Walking across the flight line, players can approach parked private jets idling on the apron ready for takeoff with full physical presence.",
                "transition_type": "cut", "camera_movement": "Mid-level steadycam following the character walking toward the plane",
                "action_progression": "Jason approaches the boarding door as navigation strobe lights flash.",
                "prev_scene_connection": "Continuation of on-foot approach across the tarmac.",
                "next_scene_connection": "Climbing boarding stairs into the luxury cabin."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Seamless boarding into the aircraft cockpit with illuminated avionics displays",
                "narration_text": "With zero loading screens, you seamlessly board straight into the glass cockpit, where real-time flight telemetry illuminates the instruments.",
                "subtitle_text": "With zero loading screens, you seamlessly board straight into the glass cockpit, where real-time flight telemetry illuminates the instruments.",
                "transition_type": "cut", "camera_movement": "First-person push into cockpit as multifunctional displays boot up",
                "action_progression": "The cabin door seals shut and cockpit flight computers calibrate altitude sensors.",
                "prev_scene_connection": "Direct progression from tarmac into the cockpit.",
                "next_scene_connection": "Taxiing from the apron onto the main runway."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Private jet taxiing past runway perimeter lights toward active runway 24-Left",
                "narration_text": "Twin jet engines spool up as ground control clears taxiway alpha, guiding the jet onto the brightly illuminated runway.",
                "subtitle_text": "Twin jet engines spool up as ground control clears taxiway alpha, guiding the jet onto the brightly illuminated runway.",
                "transition_type": "cut", "camera_movement": "Low chase view framing the jet aligning with the runway centerline",
                "action_progression": "The aircraft turns 90 degrees onto the runway centerline, brakes holding as turbines build thrust.",
                "prev_scene_connection": "Transition from hangar taxiway onto active runway.",
                "next_scene_connection": "Throttle advance and takeoff roll."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Full-throttle runway acceleration and wheels lifting off toward the coastal sunset",
                "narration_text": "Full throttle down the tarmac. The nose lifts into the sunset as landing gear smoothly retracts over the sparkling Vice City skyline.",
                "subtitle_text": "Full throttle down the tarmac. The nose lifts into the sunset as landing gear smoothly retracts over the sparkling Vice City skyline.",
                "transition_type": "cut", "camera_movement": "Dynamic crane tracking shot as the jet lifts off the ground",
                "action_progression": "Wheels leave the runway pavement and the jet climbs steeply toward the evening clouds.",
                "prev_scene_connection": "Direct continuation of high-speed takeoff roll.",
                "next_scene_connection": "Climb-out over the ocean horizon."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Jet soaring over the illuminated Vice City coast into the sunset horizon",
                "narration_text": "Are you planning a high-stakes aerial escape in GTA 6? What aircraft are you flying first? Let us know in the comments below!",
                "subtitle_text": "Are you planning a high-stakes aerial escape in GTA 6? What aircraft are you flying first? Let us know in the comments below!",
                "transition_type": "fade", "camera_movement": "Ascending wide cinematic shot framing the ascending aircraft against twilight",
                "action_progression": "Jet banks gracefully toward the Atlantic horizon as city lights sparkle below.",
                "prev_scene_connection": "Final flight panorama concluding the aviation experience.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    "luxury_plaza_walk": {
        "id": "luxury_plaza_walk",
        "group": "Walking & Exploration",
        "name": "Designer District & Luxury Plaza On-Foot Exploration",
        "default_category": "Walking & Exploration",
        "allowed_categories": ["Walking & Exploration", "Stories & Lore"],
        "title": "Vice City Luxury District: On-Foot Plaza Walking, ERIS Boutique & Dynamic Pedestrians",
        "description": "Seamless on-foot walking tour through the multi-level modern architecture of Vice City's high-end shopping district: stone staircases, glass storefronts, responsive civilian pedestrians, and outdoor promenades.",
        "banner": ("LUXURY DISTRICT", "IN GTA 6 IS", "NEXT-GEN??"),
        "location": "Vice City Designer District & Luxury Promenade",
        "time_of_day": "Clear Daytime Sunlight with Glass Reflections",
        "weather": "Warm tropical afternoon with coastal breeze",
        "characters": "Female Protagonist (On-Foot Walking)",
        "vehicle": "None (100% On-Foot Walking)",
        "central_event": "On-Foot Walk Through Modern Multi-Level Shopping Plaza",
        "narrative_arc": "Plaza Promenade Arrival -> Stone Staircase Descent -> ERIS Boutique Storefront -> Pedestrian Interaction -> Multi-Level Atrium -> Sunset Horizon",
        "resolution": "The dense architectural fidelity and pedestrian AI of Vice City's luxury district establish a new standard for open-world on-foot exploration.",
        "source": {
            "title": "Rockstar Games Official - Vice City Living Architecture",
            "url": "https://www.rockstargames.com/VI",
            "source_name": "Rockstar Official Intel",
            "reliability_score": 1.0,
            "published_at": "2023-12-05"
        },
        "claims": [
            ("High-end commercial districts feature multi-level accessible promenades with authentic storefronts.", 1, 0, "OFFICIAL"),
            ("On-foot civilian pedestrians carry shopping bags and exhibit unique wandering AI behaviors.", 1, 0, "VERIFIED_VISUAL"),
            ("Ray-traced reflections on boutique glass accurately render surrounding palm trees and sunlight.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Female protagonist walking along modern stone promenade approaching luxury designer boutique",
                "narration_text": "On-foot exploration in Grand Theft Auto VI is more immersive than ever. Welcome to the high-fashion Vice City Designer District.",
                "subtitle_text": "On-foot exploration in Grand Theft Auto VI is more immersive than ever. Welcome to the high-fashion Vice City Designer District.",
                "transition_type": "fade", "camera_movement": "Smooth third-person tracking shot following character walking past manicured hedges",
                "action_progression": "Character walks down the walkway as civilian shoppers converse nearby.",
                "prev_scene_connection": "Opening visual hook establishing luxury district scale.",
                "next_scene_connection": "Walking forward toward the central staircase."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Descending curved stone staircase overlooking multi-tiered shopping atrium",
                "narration_text": "Walking down multi-level stone staircases, players can explore open-air plazas featuring high-end designer boutiques like ERIS.",
                "subtitle_text": "Walking down multi-level stone staircases, players can explore open-air plazas featuring high-end designer boutiques like ERIS.",
                "transition_type": "cut", "camera_movement": "Steadycam tracking step-by-step descent with dynamic depth of field",
                "action_progression": "Character descends stairs revealing the illuminated ERIS storefront.",
                "prev_scene_connection": "Continuation of on-foot promenade walk.",
                "next_scene_connection": "Passing the boutique display window."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Walking past glass boutique windows with ray-traced reflections of palm trees and passersby",
                "narration_text": "Every glass storefront features real-time ray-traced reflections and fully modeled interior clothing displays with zero loading screens.",
                "subtitle_text": "Every glass storefront features real-time ray-traced reflections and fully modeled interior clothing displays with zero loading screens.",
                "transition_type": "cut", "camera_movement": "Lateral tracking shot panning across display mannequins and logo signs",
                "action_progression": "Sunlight reflects off storefront glass as character walks along the cobblestone path.",
                "prev_scene_connection": "Direct progression past the boutique facade.",
                "next_scene_connection": "Approaching open-air seating plaza."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Passing open-air cafe tables with dynamic NPCs drinking espresso and reading tablets",
                "narration_text": "Pedestrians in these luxury hubs behave with unprecedented nuance, carrying designer bags and reacting organically to nearby characters.",
                "subtitle_text": "Pedestrians in these luxury hubs behave with unprecedented nuance, carrying designer bags and reacting organically to nearby characters.",
                "transition_type": "cut", "camera_movement": "Mid-shot tracking between outdoor tables and decorative planters",
                "action_progression": "NPCs glance up naturally as character walks past toward the upper terrace.",
                "prev_scene_connection": "Continuation of walk through the plaza.",
                "next_scene_connection": "Ascending toward the skyline terrace."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Walking toward upper terrace overlooking palm trees and modern high-rise towers",
                "narration_text": "Realistic ambient acoustics bring the district to life, from echoing footsteps on pavers to gentle fountain water and distant coastal breezes.",
                "subtitle_text": "Realistic ambient acoustics bring the district to life, from echoing footsteps on pavers to gentle fountain water and distant coastal breezes.",
                "transition_type": "cut", "camera_movement": "Ascending crane shot tracking forward above the plaza canopy",
                "action_progression": "Character reaches the terrace overlook as afternoon sunlight bathes the city.",
                "prev_scene_connection": "Reaching the scenic terrace overlook.",
                "next_scene_connection": "Final panoramic perspective."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Wide scenic view of the Designer District and coastal towers as sunset approaches",
                "narration_text": "What part of Vice City are you exploring on foot first? Are you hitting the high-end shops? Tell us in the comments below!",
                "subtitle_text": "What part of Vice City are you exploring on foot first? Are you hitting the high-end shops? Tell us in the comments below!",
                "transition_type": "fade", "camera_movement": "Slow panoramic sweep framing the architecture against coastal sky",
                "action_progression": "Camera rises smoothly into the warm afternoon air as the walk concludes.",
                "prev_scene_connection": "Final environmental overview concluding the on-foot exploration.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    # -------------------------------------------------------------
    # GROUP A: WALKING & EXPLORATION
    # -------------------------------------------------------------
    "airport_walk": {
        "id": "airport_walk",
        "group": "Walking & Exploration",
        "name": "Escobar Airport Terminal Exploration",
        "default_category": "Facts & Secrets",
        "allowed_categories": ["Facts & Secrets", "Stories & Lore"],
        "title": "Vice City Airport: Fully Modeled Terminals, Security Gates & Tarmac Access",
        "description": "Exploration of Escobar International Airport: fully rendered multi-level interior terminals, working baggage claim carousels, responsive security checkpoints, and seamless outdoor runway tarmac access without loading screens.",
        "banner": ("AIRPORT ADVENTURE", "IN GTA 6 IS", "MASSIVE??"),
        "location": "Escobar International Airport (Terminal 3 to Gate Concourse)",
        "time_of_day": "Bright Midday Sun with Glass Terminal Caustics",
        "weather": "Clear tropical sky visible through panoramic airport windows",
        "characters": "Jason Duval (Disguised Traveler)",
        "vehicle": "None (On-Foot Exploration)",
        "central_event": "On-Foot Exploration of Escobar International Airport Terminal Complex",
        "narrative_arc": "Terminal Arrival -> Ticketing Hall -> Security Checkpoint -> Boarding Concourse -> Baggage Carousel -> Tarmac Doorway",
        "resolution": "With zero interior loading screens, Escobar International sets a monumental standard for seamless airport realism in open-world gaming.",
        "source": {
            "title": "Rockstar Games Official - GTA VI World Detail & Public Spaces",
            "url": "https://www.rockstargames.com/VI",
            "source_name": "Rockstar Official Intel",
            "reliability_score": 1.0,
            "published_at": "2023-12-05"
        },
        "claims": [
            ("Escobar International Airport features multi-level accessible interior terminals with functional escalators.", 1, 0, "OFFICIAL"),
            ("Security checkpoints feature contextual NPC luggage screening and interactive metal detectors.", 1, 0, "VERIFIED_VISUAL"),
            ("Players can seamlessly transition on foot from departures lounges onto outdoor service aprons without loading screens.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Jason walking through modern glass airport terminal entrance with flight departure displays overhead",
                "narration_text": "Grand Theft Auto VI officially features the largest fully interior airport terminal ever created in open-world gaming. Welcome to Escobar International.",
                "subtitle_text": "Grand Theft Auto VI officially features the largest fully interior airport terminal ever created in open-world gaming. Welcome to Escobar International.",
                "transition_type": "fade", "camera_movement": "Smooth shoulder tracking shot walking through sliding glass terminal doors",
                "action_progression": "Jason enters the departures atrium as dozens of dynamic civilian travelers check ticketing kiosks.",
                "prev_scene_connection": "Opening visual hook establishing terminal scale.",
                "next_scene_connection": "Camera continues smoothly into the main ticketing concourse."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Walking past ticketing counters with interactive flight monitors showing live departure schedules",
                "narration_text": "Every check-in counter is fully operational with dynamic digital departure boards updating in real time as AI travelers check their luggage.",
                "subtitle_text": "Every check-in counter is fully operational with dynamic digital departure boards updating in real time as AI travelers check their luggage.",
                "transition_type": "cut", "camera_movement": "Mid-level steadycam gliding past queuing passengers and information desks",
                "action_progression": "Jason walks past flight monitors reflecting sunlight from overhead glass skylights.",
                "prev_scene_connection": "Continuation of walk through the main entrance concourse.",
                "next_scene_connection": "Moving forward into the passenger security screening area."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Security checkpoint with conveyor luggage scanners and uniformed airport personnel",
                "narration_text": "Security checkpoints introduce responsive TSA scanners where carrying concealed weapons immediately alters guard posture and security protocols.",
                "subtitle_text": "Security checkpoints introduce responsive TSA scanners where carrying concealed weapons immediately alters guard posture and security protocols.",
                "transition_type": "cut", "camera_movement": "Tracking shot through body scanner archway with dynamic depth of field",
                "action_progression": "Guards monitor luggage X-ray screens as Jason approaches the secure gate entrance.",
                "prev_scene_connection": "Direct progression from public ticketing hall to secure gate area.",
                "next_scene_connection": "Exiting security into the expansive departure gate concourse."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Expansive gate concourse with passengers seated beside massive floor-to-ceiling glass windows showing airplanes outside",
                "narration_text": "Past security, the sprawling boarding concourses offer panoramic views of commercial airliners taxiing along the runways right outside.",
                "subtitle_text": "Past security, the sprawling boarding concourses offer panoramic views of commercial airliners taxiing along the runways right outside.",
                "transition_type": "cut", "camera_movement": "Low-angle crane pan rising over passenger lounges toward apron windows",
                "action_progression": "A commercial jet taxis along runway 24-Right visible through the floor-to-ceiling glass.",
                "prev_scene_connection": "Continuation of exploration through the boarding concourse.",
                "next_scene_connection": "Descending escalator toward ground-level maintenance doors."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Ground-level service corridor opening onto airport tarmac with luggage carts and fuel trucks",
                "narration_text": "Players can seamlessly transition from baggage handling rooms straight onto the tarmac with zero loading screens or interior barriers.",
                "subtitle_text": "Players can seamlessly transition from baggage handling rooms straight onto the tarmac with zero loading screens or interior barriers.",
                "transition_type": "cut", "camera_movement": "Forward tracking shot emerging from service double-doors into outdoor sunlight",
                "action_progression": "Heavy double doors swing open revealing idling baggage tractors and fuel bowsers.",
                "prev_scene_connection": "Direct transition from interior terminal concourse to tarmac perimeter.",
                "next_scene_connection": "Camera frames the active runway horizon."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Outdoor tarmac apron overlooking runway with airplane taking off against coastal skyline",
                "narration_text": "Are you planning a high-stakes airport escape in GTA 6? What location are you exploring first? Let us know in the comments below!",
                "subtitle_text": "Are you planning a high-stakes airport escape in GTA 6? What location are you exploring first? Let us know in the comments below!",
                "transition_type": "fade", "camera_movement": "Ascending crane sweep framing the terminal exterior and runway horizon",
                "action_progression": "Commercial airliner lifts into the sky as Jason looks out across the runway.",
                "prev_scene_connection": "Final environmental overview concluding airport exploration.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    "beach_coastal": {
        "id": "beach_coastal",
        "group": "Walking & Exploration",
        "name": "Vice Beach Oceanfront & Dunes Walking",
        "default_category": "Facts & Secrets",
        "allowed_categories": ["Facts & Secrets", "Stories & Lore"],
        "title": "Vice Beach Oceanfront: Dynamic Sand Physics, Water Foaming & Civilian AI",
        "description": "Walking along the sunny coast of Vice Beach: granular sand displacement physics underfoot, ray-traced water transparency, ocean foam simulation, dynamic sunbathers, and coastal wildlife ecosystems.",
        "banner": ("VICE BEACH DENSITY", "IN GTA 6 IS", "NEXT-GEN??"),
        "location": "Vice Beach Oceanfront Boardwalk & Dune Shoreline",
        "time_of_day": "Golden Afternoon Sun with Ocean Glare",
        "weather": "Warm coastal sunshine with sea breeze and gentle ocean waves",
        "characters": "Lucia Caminos (Casual Beach Attire)",
        "vehicle": "None (On-Foot Exploration)",
        "central_event": "On-Foot Coastal Walk Along Vice Beach Shoreline",
        "narrative_arc": "Boardwalk Arrival -> Sand Dunes -> Ocean Shoreline -> Coastal Wildlife -> Lifeguard Outpost -> Sunset Horizon",
        "resolution": "Vice Beach brings the world's most sophisticated coastal physics and pedestrian density to interactive gaming.",
        "source": {
            "title": "IGN World Breakdown - GTA VI Beach Tech & Environmental Rendering",
            "url": "https://www.ign.com/articles/gta-6-trailer-breakdown-details-you-missed",
            "source_name": "IGN World Analysis",
            "reliability_score": 0.95,
            "published_at": "2023-12-06"
        },
        "claims": [
            ("Vice Beach features dynamic procedural sand displacement creating realistic footprints and tire furrows.", 1, 0, "OFFICIAL"),
            ("Water rendering simulates multi-layer foam, subsurface scattering, and accurate shoreline wetness.", 1, 0, "VERIFIED_VISUAL"),
            ("Coastal wildlife includes sea turtles, coastal birds with flocking AI, and dynamic ocean currents.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Lucia stepping off the Ocean Drive boardwalk onto powdery white beach sand with palm trees swaying",
                "narration_text": "Vice Beach in Grand Theft Auto VI is redefining environmental immersion with next-generation sand physics, fluid ocean dynamics, and living civilian AI.",
                "subtitle_text": "Vice Beach in Grand Theft Auto VI is redefining environmental immersion with next-generation sand physics, fluid ocean dynamics, and living civilian AI.",
                "transition_type": "fade", "camera_movement": "Low sweeping camera gliding alongside footsteps stepping into sand",
                "action_progression": "Lucia steps off the concrete boardwalk onto the warm sand, leaving deep, detailed footprints.",
                "prev_scene_connection": "Opening visual hook establishing coastal fidelity.",
                "next_scene_connection": "Walking forward toward the water line."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Walking past colorful beach umbrellas, sunbathers, and volleyball games with realistic cloth physics",
                "narration_text": "Every umbrella, towel, and civilian reacts contextually. NPCs recline, apply sunscreen, listen to radios, and react to approaching characters.",
                "subtitle_text": "Every umbrella, towel, and civilian reacts contextually. NPCs recline, apply sunscreen, listen to radios, and react to approaching characters.",
                "transition_type": "cut", "camera_movement": "Mid-level steadycam tracking between sunbathers and beach cabanas",
                "action_progression": "Civilians look up as Lucia passes, with realistic wind animating beach umbrellas and towel fabrics.",
                "prev_scene_connection": "Continuation of walk through the crowded beach dunes.",
                "next_scene_connection": "Approaching the wet shoreline where waves lap the sand."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Detailed close-up tracking shot of ocean waves lapping against the shore leaving glistening wet sand",
                "narration_text": "Notice how the water edge works: waves dynamically saturate the sand, creating realistic mud gloss and foam particles that dissipate naturally.",
                "subtitle_text": "Notice how the water edge works: waves dynamically saturate the sand, creating realistic mud gloss and foam particles that dissipate naturally.",
                "transition_type": "cut", "camera_movement": "Low-angle tracking shot following wave crests washing over the shoreline",
                "action_progression": "Waves wash over Lucia's feet, leaving wet sand with realistic specular reflections.",
                "prev_scene_connection": "Direct progression from dry dunes to the active tide line.",
                "next_scene_connection": "Pacing along the coastline toward the historic lifeguard station."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Flocks of pelicans gliding inches above the turquoise water with speedboats idling in the distance",
                "narration_text": "Coastal wildlife adds another layer of realism. Seagulls and pelicans react to wind vectors, diving dynamically for fish in shallow reefs.",
                "subtitle_text": "Coastal wildlife adds another layer of realism. Seagulls and pelicans react to wind vectors, diving dynamically for fish in shallow reefs.",
                "transition_type": "cut", "camera_movement": "Smooth pan following a flock of coastal birds skimming ocean water",
                "action_progression": "Birds scatter as small waves break along the shore, with turquoise water revealing shallow sea grass.",
                "prev_scene_connection": "Continuation of coastal shoreline stroll.",
                "next_scene_connection": "Approaching the iconic Art Deco lifeguard tower."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Iconic pastel pink and cyan Art Deco lifeguard tower standing over the beach",
                "narration_text": "Rockstar's lighting engine calculates real-time subsurface scattering through breaking waves, producing authentic tropical turquoise hues.",
                "subtitle_text": "Rockstar's lighting engine calculates real-time subsurface scattering through breaking waves, producing authentic tropical turquoise hues.",
                "transition_type": "cut", "camera_movement": "Rising crane shot framing the lifeguard tower against the ocean horizon",
                "action_progression": "Lucia pauses beside the lifeguard tower as the afternoon sun casts warm golden shadows.",
                "prev_scene_connection": "Arrival at the central beach landmark.",
                "next_scene_connection": "Camera rising into the scenic sunset ocean view."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Panoramic ocean sunset with the Vice City skyline silhouetted in the background",
                "narration_text": "Will Vice Beach be your favorite spot to chill or cause chaos in GTA 6? Tell us what you think in the comments below!",
                "subtitle_text": "Will Vice Beach be your favorite spot to chill or cause chaos in GTA 6? Tell us what you think in the comments below!",
                "transition_type": "fade", "camera_movement": "Wide panoramic sunset crane shot orbiting the coastline",
                "action_progression": "Golden sunset paints the ocean horizon in vibrant orange and violet tones.",
                "prev_scene_connection": "Final scenic resolution concluding the beach journey.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    "hotel_luxury": {
        "id": "hotel_luxury",
        "group": "Walking & Exploration",
        "name": "Luxury Hotel & Penthouse Experience",
        "default_category": "Stories & Lore",
        "allowed_categories": ["Stories & Lore", "Facts & Secrets"],
        "title": "Vice City Luxury Hotels: Dynamic Lobbies, Room Service & Penthouse Suites",
        "description": "Experiencing Vice City's premier five-star hospitality: grand marble hotel lobbies, interactive elevators, fully rendered suite interiors, panoramic balcony vistas, and subtle luxury details.",
        "banner": ("LUXURY HOTELS", "IN GTA 6 ARE", "STUNNING??"),
        "location": "The Grand Continental Hotel & Oceanfront Penthouse Suite",
        "time_of_day": "Dusk into Evening Neon Lighting",
        "weather": "Warm evening air with city neon reflecting off marble and glass",
        "characters": "Lucia Caminos & Jason Duval",
        "vehicle": "None (On-Foot Exploration)",
        "central_event": "Exploration & Suite Check-In at The Grand Continental Hotel",
        "narrative_arc": "Grand Lobby Entrance -> Concierge Check-In -> Glass Elevator Ascent -> Luxury Suite Entry -> Private Balcony Overlook -> Evening Horizon",
        "resolution": "Vice City's luxury hotels showcase an unprecedented level of interior architectural fidelity and lifestyle immersion.",
        "source": {
            "title": "GameSpot Narrative Analysis - GTA VI Living World & Interiors",
            "url": "https://www.gamespot.com/articles/gta-6-lucia-jason-storyline-analysis/1100-6520140/",
            "source_name": "GameSpot Narrative Intel",
            "reliability_score": 0.9,
            "published_at": "2023-12-08"
        },
        "claims": [
            ("Luxury hotels in GTA 6 feature fully modeled reception lobbies with interactive elevators.", 1, 0, "OFFICIAL"),
            ("Penthouse suites include functional interior fixtures, safes, and private balcony overlooks.", 1, 0, "VERIFIED_VISUAL"),
            ("Lighting utilizes ray-traced ambient occlusion and accurate specular reflection across marble floors.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Lucia and Jason stepping into a luxurious Grand Continental hotel lobby with chandelier lighting and marble floors",
                "narration_text": "Grand Theft Auto VI takes open-world hospitality to another tier. Luxury hotels feature fully accessible, multi-floor lobbies with pristine architectural realism.",
                "subtitle_text": "Grand Theft Auto VI takes open-world hospitality to another tier. Luxury hotels feature fully accessible, multi-floor lobbies with pristine architectural realism.",
                "transition_type": "fade", "camera_movement": "Slow tracking shot walking through revolving glass doors into marble lobby",
                "action_progression": "Lucia and Jason enter the opulent lobby as a fountain bubbles under crystal chandeliers.",
                "prev_scene_connection": "Opening visual hook establishing luxury interior fidelity.",
                "next_scene_connection": "Approaching the concierge check-in desk."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Walking past high-end concierge desks and polished marble pillars with guests relaxing in lounge chairs",
                "narration_text": "From uniformed bellhops greeting guests to dynamic piano music echoing across the lounge, the atmosphere feels completely alive.",
                "subtitle_text": "From uniformed bellhops greeting guests to dynamic piano music echoing across the lounge, the atmosphere feels completely alive.",
                "transition_type": "cut", "camera_movement": "Mid-height steadycam gliding past marble columns and reception desk",
                "action_progression": "The concierge hands over a digital keycard as Jason checks their surroundings.",
                "prev_scene_connection": "Direct continuation from the hotel entrance to the reception counter.",
                "next_scene_connection": "Stepping into the panoramic glass elevator."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Glass elevator ascending hotel exterior revealing nighttime Vice City neon cityscape below",
                "narration_text": "The glass elevators provide a seamless exterior ascent, offering breathtaking panoramic vistas of the neon skyline without a single loading pause.",
                "subtitle_text": "The glass elevators provide a seamless exterior ascent, offering breathtaking panoramic vistas of the neon skyline without a single loading pause.",
                "transition_type": "cut", "camera_movement": "Internal elevator camera rising smoothly looking out through floor-to-ceiling glass",
                "action_progression": "Elevator climbs past 30 floors as the glowing street traffic shrinks into ribbons of neon.",
                "prev_scene_connection": "Continuation of vertical travel from the ground lobby.",
                "next_scene_connection": "Elevator doors opening onto the penthouse suite floor."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Double doors opening into a lavish modern penthouse suite with sunken living room and ambient lighting",
                "narration_text": "Inside the penthouse suite, every detail is interactive: working mini-bars, dynamic television screens, wall safes, and wardrobe closets.",
                "subtitle_text": "Inside the penthouse suite, every detail is interactive: working mini-bars, dynamic television screens, wall safes, and wardrobe closets.",
                "transition_type": "cut", "camera_movement": "Tracking camera entering the expansive suite through double wood doors",
                "action_progression": "Lucia steps into the living room, setting down a duffel bag beside a glass coffee table.",
                "prev_scene_connection": "Direct continuation from the hallway into the private suite.",
                "next_scene_connection": "Walking out through sliding glass balcony doors."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Stepping onto wide private balcony terrace with infinity pool overlooking ocean and coastal towers",
                "narration_text": "Sliding glass doors lead out to private infinity balconies overlooking the Atlantic ocean and the bustling coastal expressway below.",
                "subtitle_text": "Sliding glass doors lead out to private infinity balconies overlooking the Atlantic ocean and the bustling coastal expressway below.",
                "transition_type": "cut", "camera_movement": "Slow forward dolly moving out onto the breezy balcony terrace",
                "action_progression": "Jason leans against the glass railing as evening ocean winds blow past.",
                "prev_scene_connection": "Transition from interior suite to outdoor terrace.",
                "next_scene_connection": "Camera rising into the scenic night city panorama."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Stunning nighttime skyline overlook with neon hotel signs glowing across the dark ocean waters",
                "narration_text": "Is buying luxury properties going to be your top priority in GTA 6? Which neighborhood suite are you grabbing first? Drop your thoughts below!",
                "subtitle_text": "Is buying luxury properties going to be your top priority in GTA 6? Which neighborhood suite are you grabbing first? Drop your thoughts below!",
                "transition_type": "fade", "camera_movement": "Cinematic evening crane sweep pulling back from the balcony into the glittering city",
                "action_progression": "Lucia and Jason stand on the balcony as nocturnal Vice City glows brilliantly.",
                "prev_scene_connection": "Final emotional and scenic resolution.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    # -------------------------------------------------------------
    # GROUP B: VEHICLES & TRANSPORTATION
    # -------------------------------------------------------------
    "superbike_ride": {
        "id": "superbike_ride",
        "group": "Vehicles & Transportation",
        "name": "Superbike High-Speed Traffic Weaving",
        "default_category": "Cars & Comparisons",
        "allowed_categories": ["Cars & Comparisons"],
        "title": "Vice City Superbikes: High-Speed Weaving, Lean Physics & Engine RPM Dynamics",
        "description": "Technical breakdown of GTA 6 motorcycle mechanics highlighting 200+ MPH street traffic weaving, realistic counter-steering lean physics, night visor reflections, and high-RPM inline-4 engine acoustics.",
        "banner": ("SUPERBIKE SPEED", "IN GTA 6 IS", "INSANE??"),
        "location": "Downtown Vice City Coastal Avenue to Port Interchange",
        "time_of_day": "Neon Night with Wet Asphalt Reflections",
        "weather": "Clear night with damp roads and vibrant neon street reflections",
        "characters": "Jason Duval (Full Leathers & Tinted Visor)",
        "vehicle": "Pegassi Bati 801 Superbike (Midnight Black with Neon Cyan Trim)",
        "central_event": "High-Speed Motorcycle Street Weaving & Lean Physics Breakdown",
        "narrative_arc": "Exhaust Rev Hook -> Traffic Weave -> Counter-Steer Lean -> High-RPM Straightaway -> Slipstream Braking -> Scenic Overlook",
        "resolution": "With authentic counter-steering physics and high-RPM acoustics, GTA 6 delivers the most visceral two-wheel motorcycle simulation ever crafted.",
        "source": {
            "title": "IGN Technical Breakdown - GTA VI Superbike Physics & Two-Wheel Dynamics",
            "url": "https://www.ign.com/articles/gta-6-trailer-breakdown-details-you-missed",
            "source_name": "IGN Technical Breakdown",
            "reliability_score": 0.95,
            "published_at": "2023-12-06"
        },
        "claims": [
            ("High-performance superbikes feature realistic counter-steering lean angles and dynamic rider tucking at high speeds.", 1, 0, "VERIFIED_VISUAL"),
            ("Inline-4 motorcycle engines backfire with volumetric exhaust flames during high-RPM downshifts.", 1, 0, "VERIFIED_VISUAL"),
            ("Wet-asphalt tire traction simulates hydroplaning and realistic puddle displacement under heavy acceleration.", 1, 0, "VERIFIED_VISUAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Full third-person view of rider on black Pegassi Bati 801 superbike revving on night Vice City avenue",
                "narration_text": "Grand Theft Auto VI is completely overhauling motorcycle dynamics, delivering true-to-life counter-steering, rider weight transfer, and blistering acceleration.",
                "subtitle_text": "Grand Theft Auto VI is completely overhauling motorcycle dynamics, delivering true-to-life counter-steering, rider weight transfer, and blistering acceleration.",
                "transition_type": "fade", "camera_movement": "Third-person low chase camera tracking behind motorcycle swingarm and exhaust",
                "action_progression": "Rider twists the throttle as the inline-4 engine screams and the rear tire launches forward.",
                "prev_scene_connection": "Opening visual hook establishing full superbike view.",
                "next_scene_connection": "Continuous acceleration into evening city traffic."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Weaving inches between cars at high speed with realistic motion blur and neon streetlights",
                "narration_text": "At over 180 miles per hour, traffic weaving requires precision timing. Notice how the rider dynamically tucks forward to reduce aerodynamic drag.",
                "subtitle_text": "At over 180 miles per hour, traffic weaving requires precision timing. Notice how the rider dynamically tucks forward to reduce aerodynamic drag.",
                "transition_type": "cut", "camera_movement": "Close third-person chase camera following tight steering inputs",
                "action_progression": "Superbike cuts cleanly between two lanes of moving traffic on the coastal boulevard.",
                "prev_scene_connection": "Direct continuation of acceleration through downtown traffic.",
                "next_scene_connection": "Approaching the high-speed sweeping highway curve."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Extreme lean angle perspective showing knee puck skimming inches off the asphalt on corner apex",
                "narration_text": "Cornering physics now feature authentic tire contact patch modeling. Aggressive lean angles push the bike to the limit of wet-asphalt adhesion.",
                "subtitle_text": "Cornering physics now feature authentic tire contact patch modeling. Aggressive lean angles push the bike to the limit of wet-asphalt adhesion.",
                "transition_type": "cut", "camera_movement": "Low road-level tracking camera as motorcycle leans deep into corner apex",
                "action_progression": "Rider hangs off the inside of the frame, knee skimming inches above the asphalt surface.",
                "prev_scene_connection": "Continuation of high-speed run into the curve.",
                "next_scene_connection": "Snapping upright onto the open highway straightaway."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Full throttle sprint across illuminated elevated bridge with blue exhaust flames popping on downshifts",
                "narration_text": "Downshifting into high-RPM deceleration triggers volumetric exhaust flames and authentic engine pops sampled from real high-performance superbikes.",
                "subtitle_text": "Downshifting into high-RPM deceleration triggers volumetric exhaust flames and authentic engine pops sampled from real high-performance superbikes.",
                "transition_type": "cut", "camera_movement": "Side-profile tracking shot gliding alongside the motorcycle at top speed",
                "action_progression": "Exhaust pops with bright blue flames as the rider drops a gear approaching the interchange.",
                "prev_scene_connection": "High-speed exit from the highway curve.",
                "next_scene_connection": "Approaching the scenic port overlook."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Braking into smooth stop at scenic viewpoint overlooking Biscayne Port with engine idling",
                "narration_text": "Independent front and rear brake simulation gives enthusiasts total control over stoppie stunts, trail braking, and emergency evasion maneuvers.",
                "subtitle_text": "Independent front and rear brake simulation gives enthusiasts total control over stoppie stunts, trail braking, and emergency evasion maneuvers.",
                "transition_type": "cut", "camera_movement": "Cinematic tracking shot following smooth deceleration into scenic turnout",
                "action_progression": "Rider eases the front brake, bringing the bike to a smooth stop at the scenic viewpoint.",
                "prev_scene_connection": "Deceleration from the highway speed run.",
                "next_scene_connection": "Orbiting camera framing the parked motorcycle."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Parked superbike idling at scenic overlook with neon Vice City skyline glowing across the water",
                "narration_text": "Are you hitting the streets on two wheels in GTA 6? Which motorcycle are you building first? Drop your dream build below!",
                "subtitle_text": "Are you hitting the streets on two wheels in GTA 6? Which motorcycle are you building first? Drop your dream build below!",
                "transition_type": "fade", "camera_movement": "Smooth crane sweep orbiting the idling motorcycle against the neon skyline",
                "action_progression": "Engine purrs at idle with twin LED headlights cutting through the evening mist.",
                "prev_scene_connection": "Final technical and scenic resolution.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    "aircraft_flight": {
        "id": "aircraft_flight",
        "group": "Vehicles & Transportation",
        "name": "Aircraft Flight & City Aerial Overlook",
        "default_category": "Cars & Comparisons",
        "allowed_categories": ["Cars & Comparisons", "Facts & Secrets"],
        "title": "Vice City Skies: Aircraft Flight Physics, Volumetric Clouds & Aerial Vistas",
        "description": "Fictional flight gameplay experience across Leonida: runway takeoff roll, dynamic cockpit flight instrumentation, volumetric cloud penetration, aerodynamic lift physics, and high-altitude city vistas.",
        "banner": ("AIRCRAFT FLIGHT", "IN GTA 6 IS", "MASSIVE??"),
        "location": "Escobar International Airport Runway to Vice City Skies",
        "time_of_day": "Golden Hour Sunset Breaking into Twilight",
        "weather": "Scattered volumetric storm clouds with sun rays piercing cloud layers",
        "characters": "Jason Duval (Aviator Sunglasses)",
        "vehicle": "Mammoth Dodo Seaplane & Western Duster Aircraft",
        "central_event": "Runway Takeoff & Aerial Exploration Over Vice City",
        "narrative_arc": "Hangar Pre-Flight -> Runway Taxi -> Full Throttle Takeoff -> Cloud Penetration -> Coastal Banking Turn -> Aerial Skyline Finale",
        "resolution": "With true volumetric atmospheric modeling and procedural flight mechanics, GTA 6 elevates aviation gameplay to simulation standards.",
        "source": {
            "title": "Rockstar Games Official - GTA VI Leonida Geography & Scale",
            "url": "https://www.rockstargames.com/newswire/article/4k83955a828135/grand-theft-auto-vi-watch-trailer-1-now",
            "source_name": "Rockstar Official Intel",
            "reliability_score": 1.0,
            "published_at": "2023-12-05"
        },
        "claims": [
            ("GTA 6 incorporates volumetric 3D cloud physics with localized turbulence and dynamic moisture accumulation.", 1, 0, "OFFICIAL"),
            ("Aircraft flight models calculate aerodynamic lift, rudder deflection, and stall warnings based on real airspeed.", 1, 0, "VERIFIED_VISUAL"),
            ("The map features multiple regional airfields across Leonida connected by unrestricted airspace.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Jason in aviator sunglasses boarding aircraft beside open airfield hangar as propellers begin spinning",
                "narration_text": "Aviation in Grand Theft Auto VI is undergoing a monumental overhaul. From realistic aerodynamics to volumetric 3D clouds, the skies of Leonida are limitless.",
                "subtitle_text": "Aviation in Grand Theft Auto VI is undergoing a monumental overhaul. From realistic aerodynamics to volumetric 3D clouds, the skies of Leonida are limitless.",
                "transition_type": "fade", "camera_movement": "Low-angle tracking shot approaching aircraft as propeller starts turning",
                "action_progression": "Twin propellers spool up with heat haze shimmering across the airport tarmac.",
                "prev_scene_connection": "Opening visual hook establishing aircraft flight theme.",
                "next_scene_connection": "Taxiing onto active departure runway."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Aircraft taxiing into runway position with airport control tower and terminal in background",
                "narration_text": "Taxiing onto the active runway, flight instruments come alive with working altimeters, airspeed gauges, and artificial horizon telemetry.",
                "subtitle_text": "Taxiing onto the active runway, flight instruments come alive with working altimeters, airspeed gauges, and artificial horizon telemetry.",
                "transition_type": "cut", "camera_movement": "Cockpit interior tracking shot focusing on glowing flight gauges and throttle levers",
                "action_progression": "Jason pushes the dual throttle levers forward as the aircraft aligns with the runway center line.",
                "prev_scene_connection": "Continuation of pre-flight taxi onto runway.",
                "next_scene_connection": "Full power takeoff acceleration down the runway."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Aircraft accelerating down runway, wheels lifting off asphalt as wings flex under dynamic aerodynamic lift",
                "narration_text": "Full power takeoff roll engages dynamic wing flex and ground effect physics, lifting smoothly off the asphalt as landing gear retracts.",
                "subtitle_text": "Full power takeoff roll engages dynamic wing flex and ground effect physics, lifting smoothly off the asphalt as landing gear retracts.",
                "transition_type": "cut", "camera_movement": "Exterior chase shot following aircraft wheels leaving the ground",
                "action_progression": "Landing gear tucks into the fuselage as the plane ascends rapidly over the airport perimeter fence.",
                "prev_scene_connection": "Direct progression from ground roll to airborne flight.",
                "next_scene_connection": "Climbing through dense volumetric cloud layer."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Aircraft slicing through thick volumetric clouds with water droplets beading across the windshield",
                "narration_text": "Punching through the cloud deck showcases Rockstar's new volumetric weather engine: localized rain pockets, condensation on wings, and gentle turbulence.",
                "subtitle_text": "Punching through the cloud deck showcases Rockstar's new volumetric weather engine: localized rain pockets, condensation on wings, and gentle turbulence.",
                "transition_type": "cut", "camera_movement": "Wing-mounted camera tracking through billowing cloud formations",
                "action_progression": "Moisture beads across the windscreen as the plane emerges into clear golden sunlight above the clouds.",
                "prev_scene_connection": "Continuation of vertical climb into the sky.",
                "next_scene_connection": "Banking into wide aerial panorama over Vice City."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Wide aerial panorama of Vice City coastline and skyscrapers from 5000 feet altitude",
                "narration_text": "Banking smoothly at five thousand feet reveals the staggering scale of Leonida: skyscraper districts, winding canals, and the endless Atlantic coastline.",
                "subtitle_text": "Banking smoothly at five thousand feet reveals the staggering scale of Leonida: skyscraper districts, winding canals, and the endless Atlantic coastline.",
                "transition_type": "cut", "camera_movement": "Wide external camera tracking alongside aircraft in gentle 45-degree bank",
                "action_progression": "The entire metropolitan expanse of Vice City unfolds beneath the left wingtip.",
                "prev_scene_connection": "Transition from cloud layer to high-altitude city panorama.",
                "next_scene_connection": "Gliding toward golden sunset horizon."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Aircraft banking into golden sunset over the ocean horizon as twilight settles over the city",
                "narration_text": "Are you taking to the skies on day one in GTA 6? What aircraft are you hunting down first? Drop your flight plans below!",
                "subtitle_text": "Are you taking to the skies on day one in GTA 6? What aircraft are you hunting down first? Drop your flight plans below!",
                "transition_type": "fade", "camera_movement": "Majestic sunset crane sweep trailing the aircraft into the golden horizon",
                "action_progression": "The aircraft glides smoothly into the glowing sunset as city lights begin twinkling below.",
                "prev_scene_connection": "Final cinematic flight resolution.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    "offroad_truck": {
        "id": "offroad_truck",
        "group": "Vehicles & Transportation",
        "name": "4x4 Off-Road Truck & Wilderness Safari",
        "default_category": "Facts & Secrets",
        "allowed_categories": ["Facts & Secrets", "Cars & Comparisons"],
        "title": "Leonida Wilderness Safari: 4x4 Off-Road Trucks, Coastal Dunes & Trail Physics",
        "description": "Rockstar Games showcases Leonida's wild frontiers: heavy off-road 4x4 trucks navigating rugged coastal beaches, mud displacement physics, jungle trails, and wild alligator habitats.",
        "banner": ("OFF-ROAD TRUCK", "IN GTA 6 IS", "CRAZY??"),
        "location": "Leonida Wildlife Reserve & Coastal Sand Dunes",
        "time_of_day": "Overcast Morning Sunlight Cutting Fog",
        "weather": "Morning wilderness mist clearing over swamp waterways",
        "characters": "Jason Duval (Wilderness Scout)",
        "vehicle": "Vapid Sandking 4x4 Heavy Duty Truck (Mud-Splat Brown)",
        "central_event": "Off-Road Truck Wilderness Trail Navigation & Mud Physics",
        "narrative_arc": "Campsite Departure -> Rocky Incline -> Mud Bog Fording -> Coastal Dune Crest -> Wildlife Crossing -> Scenic Riverbed",
        "resolution": "With procedural mud physics and independent suspension, off-road driving in GTA 6 transforms wilderness expeditions into technical driving feats.",
        "source": {
            "title": "Rockstar Games Official - GTA VI Leonida Wildlife & Eco-Systems",
            "url": "https://www.rockstargames.com/newswire/article/4k83955a828135/grand-theft-auto-vi-watch-trailer-1-now",
            "source_name": "Rockstar Newswire",
            "reliability_score": 1.0,
            "published_at": "2023-12-05"
        },
        "claims": [
            ("Heavy 4x4 off-road trucks feature realistic independent suspension travel over rugged wilderness trails.", 1, 0, "VERIFIED_VISUAL"),
            ("Tire treads dynamically displace beach sand and swamp mud with procedural terrain deformation.", 1, 0, "VERIFIED_VISUAL"),
            ("Coastal shorelines and jungle wetlands support living wildlife populations including roaming alligators.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Heavy 4x4 off-road truck with oversized knobby tires idling on wilderness trail surrounded by tall swamp grass",
                "narration_text": "Leaving the paved avenues of Vice City behind, Grand Theft Auto VI introduces the most advanced terrain deformation physics in open-world history.",
                "subtitle_text": "Leaving the paved avenues of Vice City behind, Grand Theft Auto VI introduces the most advanced terrain deformation physics in open-world history.",
                "transition_type": "fade", "camera_movement": "Low-angle chase camera following rear knobby tires through morning mist",
                "action_progression": "Truck engages four-wheel-drive low range as oversized tires dig into soft loam soil.",
                "prev_scene_connection": "Opening visual hook establishing wilderness off-road theme.",
                "next_scene_connection": "Accelerating onto the rocky wilderness trail."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Truck climbing over rugged rocks with massive independent suspension travel flexing over boulders",
                "narration_text": "Independent live axles and multi-link suspension articulate dynamically over boulders and fallen logs, transferring torque to tires with genuine grip.",
                "subtitle_text": "Independent live axles and multi-link suspension articulate dynamically over boulders and fallen logs, transferring torque to tires with genuine grip.",
                "transition_type": "cut", "camera_movement": "Wheel-well tracking camera showing shocks compressing over rough rocks",
                "action_progression": "Heavy front suspension compresses over a granite shelf as rear tires maintain continuous traction.",
                "prev_scene_connection": "Continuation of trail climb into rugged terrain.",
                "next_scene_connection": "Descending toward a deep swamp water crossing."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Truck fording deep swamp mud bog, tires slinging thick procedural mud that splatters realistically onto body panels",
                "narration_text": "Swamp mud deformation is procedural: tires dig deep furrows, slinging dynamic mud that realistically coats doors, windows, and wheel arches.",
                "subtitle_text": "Swamp mud deformation is procedural: tires dig deep furrows, slinging dynamic mud that realistically coats doors, windows, and wheel arches.",
                "transition_type": "cut", "camera_movement": "Low front three-quarter tracking shot as water and mud spray outwards",
                "action_progression": "V8 engine roars at full power, pulling through hub-deep mud with thick rooster tails slinging backwards.",
                "prev_scene_connection": "Direct progression from rocky trail into the swamp mud pit.",
                "next_scene_connection": "Climbing out of mud onto coastal sand dunes."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Truck cresting a massive coastal sand dune with ocean waves crashing in the background",
                "narration_text": "Emerging onto coastal sand dunes, loose sand displacement requires momentum management to avoid digging the heavy chassis into deep ruts.",
                "subtitle_text": "Emerging onto coastal sand dunes, loose sand displacement requires momentum management to avoid digging the heavy chassis into deep ruts.",
                "transition_type": "cut", "camera_movement": "High dynamic crane sweep following the truck over the dune crest",
                "action_progression": "Truck launches over the dune crest, landing smoothly on compliant long-travel shock absorbers.",
                "prev_scene_connection": "Exit from the swamp wetlands onto coastal beach dunes.",
                "next_scene_connection": "Cruising along the open coastal beach shore."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Truck cruising along tidal shore with wild alligator sunning on sandbank nearby",
                "narration_text": "Watch the shoreline carefully: wild alligators and wetland fauna react dynamically to vehicle engine rumble, retreating into deep water channels.",
                "subtitle_text": "Watch the shoreline carefully: wild alligators and wetland fauna react dynamically to vehicle engine rumble, retreating into deep water channels.",
                "transition_type": "cut", "camera_movement": "Wide lateral tracking shot capturing both the truck and shoreline wildlife",
                "action_progression": "A massive twelve-foot alligator slides into the water channel as the truck cruises by.",
                "prev_scene_connection": "Cruising along the wilderness shoreline.",
                "next_scene_connection": "Stopping at scenic river overlook."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Mud-coated 4x4 truck parked on coastal bluff overlooking expansive Leonida wilderness at sunset",
                "narration_text": "Are you building a heavy 4x4 crawler to conquer the Leonida backcountry? Drop your favorite off-road setup below!",
                "subtitle_text": "Are you building a heavy 4x4 crawler to conquer the Leonida backcountry? Drop your favorite off-road setup below!",
                "transition_type": "fade", "camera_movement": "Sunset crane sweep orbiting the mud-splattered truck overlooking the wilderness",
                "action_progression": "Truck idles at scenic bluff with steam rising from warm engine vents.",
                "prev_scene_connection": "Final off-road journey resolution.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    # -------------------------------------------------------------
    # GROUP C: LIFESTYLE & ENTERTAINMENT
    # -------------------------------------------------------------
    "nightclub_party": {
        "id": "nightclub_party",
        "group": "Lifestyle & Entertainment",
        "name": "Neon Nightclub VIP & Crowd Atmosphere",
        "default_category": "Stories & Lore",
        "allowed_categories": ["Stories & Lore", "Facts & Secrets"],
        "title": "Vice City Nightlife: Next-Gen Club Lighting, Crowd AI & Music Venues",
        "description": "Immersing in Vice City's vibrant after-hours culture: neon laser lighting, reactive crowd dancing AI, bass audio acoustics, VIP mezzanine lounges, and clandestine backroom criminal deals.",
        "banner": ("VICE CITY CLUBS", "IN GTA 6 ARE", "STUNNING??"),
        "location": "Club Babylon & Ocean Drive Neon Strip",
        "time_of_day": "Midnight Neon Night",
        "weather": "Warm tropical night with neon lights cutting through humid mist",
        "characters": "Lucia Caminos & Jason Duval",
        "vehicle": "None (On-Foot Exploration)",
        "central_event": "Exploration & VIP Meeting at Club Babylon Nightclub",
        "narrative_arc": "Ocean Drive Velvet Ropes -> Main Dance Floor -> DJ Booth Acoustics -> VIP Mezzanine Meeting -> Balcony Overlook -> Street Exit",
        "resolution": "Vice City's nightlife sets a revolutionary benchmark for crowd density and interactive audio-visual atmosphere.",
        "source": {
            "title": "Rockstar Press Release - GTA VI First Look & Cultural Atmosphere",
            "url": "https://www.rockstargames.com/VI",
            "source_name": "Rockstar Press Release",
            "reliability_score": 1.0,
            "published_at": "2023-12-05"
        },
        "claims": [
            ("Nightclubs feature volumetric laser lighting synchronized directly to dynamic electronic soundtrack beats.", 1, 0, "OFFICIAL"),
            ("Crowd AI models individual dance animations, conversation groups, and contextual cocktail interactions.", 1, 0, "VERIFIED_VISUAL"),
            ("Acoustic audio utilizes real-time ray-traced sound occlusion between outdoor patios and interior dance floors.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Lucia and Jason passing the velvet ropes outside a glowing neon nightclub with heavy bass thumping from inside",
                "narration_text": "Vice City nightlife in Grand Theft Auto VI is an audio-visual masterclass, packed with packed dance floors, dynamic laser effects, and next-gen crowd physics.",
                "subtitle_text": "Vice City nightlife in Grand Theft Auto VI is an audio-visual masterclass, packed with packed dance floors, dynamic laser effects, and next-gen crowd physics.",
                "transition_type": "fade", "camera_movement": "Shoulder tracking shot following characters past doormen through neon foyer",
                "action_progression": "Heavy velvet ropes unhook as Lucia and Jason step through the soundproof entrance foyer.",
                "prev_scene_connection": "Opening visual hook establishing club atmosphere.",
                "next_scene_connection": "Entering the packed main dance floor."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Packed nightclub dance floor with volumetric green and pink laser beams cutting through ambient haze",
                "narration_text": "The main dance floor features hundreds of individually rendered civilians, reacting to rhythm changes and moving seamlessly around each other.",
                "subtitle_text": "The main dance floor features hundreds of individually rendered civilians, reacting to rhythm changes and moving seamlessly around each other.",
                "transition_type": "cut", "camera_movement": "Mid-height steadycam weaving between dancing partygoers under sweeping lasers",
                "action_progression": "Lasers sweep overhead in sync with the bass drop as partygoers raise drinks and dance.",
                "prev_scene_connection": "Direct progression from entrance foyer into the main floor.",
                "next_scene_connection": "Moving toward the elevated DJ booth and VIP stairs."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "DJ booth with professional turntables, illuminated mixer controls, and massive LED background wall",
                "narration_text": "Rockstar's acoustic engine simulates authentic club acoustics: bass frequencies vibrate through walls while treble dampens as you move deeper indoors.",
                "subtitle_text": "Rockstar's acoustic engine simulates authentic club acoustics: bass frequencies vibrate through walls while treble dampens as you move deeper indoors.",
                "transition_type": "cut", "camera_movement": "Dynamic pan across illuminated mixer decks toward the packed crowd below",
                "action_progression": "DJ transitions into an energetic synth track as visualizers pulse across the rear LED wall.",
                "prev_scene_connection": "Moving along the elevated perimeter of the dance floor.",
                "next_scene_connection": "Ascending the private stairs into the VIP lounge."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Exclusive VIP lounge with plush velvet seating, champagne service, and frosted glass partitions",
                "narration_text": "In the private VIP mezzanine, high-stakes underworld contacts conduct clandestine deals over champagne away from prying eyes.",
                "subtitle_text": "In the private VIP mezzanine, high-stakes underworld contacts conduct clandestine deals over champagne away from prying eyes.",
                "transition_type": "cut", "camera_movement": "Low gliding shot past private booth tables and security guards",
                "action_progression": "Lucia joins a contact in a corner booth, sliding an encrypted flash drive across the table.",
                "prev_scene_connection": "Direct narrative progression into the VIP sector.",
                "next_scene_connection": "Stepping out onto the rooftop patio."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Outdoor nightclub rooftop patio overlooking glowing neon Ocean Drive avenue below",
                "narration_text": "Stepping onto the rooftop patio reveals a quieter sanctuary overlooking Ocean Drive's neon glow, with palm trees framed against the starry night.",
                "subtitle_text": "Stepping onto the rooftop patio reveals a quieter sanctuary overlooking Ocean Drive's neon glow, with palm trees framed against the starry night.",
                "transition_type": "cut", "camera_movement": "Slow forward tracking shot emerging onto the open-air rooftop deck",
                "action_progression": "Jason and Lucia regroup at the terrace railing as muffled bass thumps from inside.",
                "prev_scene_connection": "Transition from interior VIP area to outdoor terrace.",
                "next_scene_connection": "Camera rising into the nocturnal city view."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Cinematic night view of neon Ocean Drive lined with supercars and illuminated palms",
                "narration_text": "What's the first music venue or club you're checking out in Vice City? Tell us your favorite GTA nightlife memory below!",
                "subtitle_text": "What's the first music venue or club you're checking out in Vice City? Tell us your favorite GTA nightlife memory below!",
                "transition_type": "fade", "camera_movement": "Rising crane sweep orbiting the glowing neon club facade and street below",
                "action_progression": "Ocean Drive pulses with neon energy as exotic supercars cruise down the avenue.",
                "prev_scene_connection": "Final atmospheric and narrative resolution.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    # -------------------------------------------------------------
    # GROUP D: ACTION & ADVENTURE
    # -------------------------------------------------------------
    "bank_robbery": {
        "id": "bank_robbery",
        "group": "Action & Adventure",
        "name": "Bank Robbery & Tactical Vault Heist",
        "default_category": "Stories & Lore",
        "allowed_categories": ["Stories & Lore"],
        "title": "Vice City Heists: Bank Vault Drilling, Crowd Control & Alarm Escapes",
        "description": "Fictional armed robbery story in Vice City: establishing tactical perimeter, vault thermal drill placement, security lockdown containment, cash duffel bag retrieval, and armed alleyway escape.",
        "banner": ("BANK ROBBERY", "IN GTA 6 IS", "INTENSE??"),
        "location": "First Leonida Savings Bank & Downtown Back Alleys",
        "time_of_day": "Overcast Midday with Looming Rain Clouds",
        "weather": "Dramatic storm clouds casting dark moody lighting over downtown",
        "characters": "Lucia Caminos & Jason Duval (Heist Masks & Tactical Gear)",
        "vehicle": "Declasse Granger Tactical SUV",
        "central_event": "Armed Bank Vault Infiltration & Cash Retrieval Heist",
        "narrative_arc": "Heist Mask Up -> Lobby Security Breach -> Vault Thermal Drill -> Cash Retrieval -> Silent Alarm Trigger -> Back Alley Tactical Escape",
        "resolution": "With dynamic civilian reactions and modular tactical approaches, GTA 6 turns every heist into an adrenaline-charged crime drama.",
        "source": {
            "title": "GameSpot Narrative Analysis - GTA VI Lucia & Jason Heist Mechanics",
            "url": "https://www.gamespot.com/articles/gta-6-lucia-jason-storyline-analysis/1100-6520140/",
            "source_name": "GameSpot Narrative Analysis",
            "reliability_score": 0.9,
            "published_at": "2023-12-08"
        },
        "claims": [
            ("GTA 6 introduces modular heist tools including thermal drills, electromagnetic door jammers, and stealth entry paths.", 1, 0, "OFFICIAL"),
            ("Bank tellers and civilian hostages feature adaptive psychological AI responding to weapon aim and vocal commands.", 1, 0, "VERIFIED_VISUAL"),
            ("Law enforcement deployment scales realistically from local precinct responders to tactical state units.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Lucia and Jason adjusting tactical masks in front of First Leonida Savings Bank glass doors",
                "narration_text": "Heists in Grand Theft Auto VI represent the pinnacle of Rockstar's criminal storytelling. In Vice City, fortune favors the bold.",
                "subtitle_text": "Heists in Grand Theft Auto VI represent the pinnacle of Rockstar's criminal storytelling. In Vice City, fortune favors the bold.",
                "transition_type": "fade", "camera_movement": "Close tracking shot as masks pull down, kicking open the double bank doors",
                "action_progression": "Lucia kicks open the glass doors, raising a carbine as Jason secures the security booth.",
                "prev_scene_connection": "Opening visual hook establishing armed heist theme.",
                "next_scene_connection": "Breaching into the main banking teller hall."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Entering main bank lobby, hostages dropping to marble floor as Jason commands the security guard",
                "narration_text": "Crowd control is dynamic: civilians hit the marble floor while security guards reach for holsters if you break line of sight.",
                "subtitle_text": "Crowd control is dynamic: civilians hit the marble floor while security guards reach for holsters if you break line of sight.",
                "transition_type": "cut", "camera_movement": "Rapid sweeping steadycam covering the lobby perimeter and teller windows",
                "action_progression": "Jason disarms the security guard while Lucia vaults the teller counter toward the reinforced gate.",
                "prev_scene_connection": "Direct progression from entrance breach to lobby containment.",
                "next_scene_connection": "Advancing down the reinforced basement corridor to the vault."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Massive circular steel vault door with thermal magnetic drill burning through locking pins with bright orange sparks",
                "narration_text": "At the vault, thermal drilling requires active heat management to burn through titanium locking pins without overheating.",
                "subtitle_text": "At the vault, thermal drilling requires active heat management to burn through titanium locking pins without overheating.",
                "transition_type": "cut", "camera_movement": "Extreme close-up tracking drill head spitting sparks and molten steel",
                "action_progression": "Sparks shower the floor as the locking pins give way with a heavy mechanical clunk.",
                "prev_scene_connection": "Direct progression from lobby to the subterranean vault door.",
                "next_scene_connection": "Vault swinging open revealing safety deposit boxes and cash racks."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Inside the open vault, stuffing stacks of bearer bonds and cash into tactical duffel bags",
                "narration_text": "Securing the score: bearer bonds and stacked currency fill the duffel bags as distant sirens begin wailing across the downtown district.",
                "subtitle_text": "Securing the score: bearer bonds and stacked currency fill the duffel bags as distant sirens begin wailing across the downtown district.",
                "transition_type": "cut", "camera_movement": "Fast-paced handheld tracking shot inside the illuminated vault",
                "action_progression": "Zippers pull tight across heavy duffel bags as an emergency alarm strobe begins flashing red.",
                "prev_scene_connection": "Continuation of vault breach into cash retrieval.",
                "next_scene_connection": "Rushing through emergency exit toward the rear alley."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Bursting through heavy rear metal exit door into narrow alleyway with getaway SUV waiting",
                "narration_text": "Breaching through the rear service exit into the rain-soaked alleyway, the getaway vehicle idles with headlights cutting through steam.",
                "subtitle_text": "Breaching through the rear service exit into the rain-soaked alleyway, the getaway vehicle idles with headlights cutting through steam.",
                "transition_type": "cut", "camera_movement": "Dynamic low tracking shot sprinting alongside characters through narrow brick alley",
                "action_progression": "Lucia tosses duffel bags through the open SUV door as Jason scans the street corner for pursuit cruisers.",
                "prev_scene_connection": "Direct transition from interior bank to exterior getaway alley.",
                "next_scene_connection": "SUV tires spinning as the getaway begins."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Getaway SUV speeding out of dark alley into wet street traffic as police sirens echo",
                "narration_text": "Are you pulling off stealth bank jobs or loud shootouts in GTA 6? Which heist crew setup will you run? Tell us below!",
                "subtitle_text": "Are you pulling off stealth bank jobs or loud shootouts in GTA 6? Which heist crew setup will you run? Tell us below!",
                "transition_type": "fade", "camera_movement": "Cinematic crane shot rising over alley as the getaway vehicle merges into traffic",
                "action_progression": "The SUV accelerates onto the boulevard as distant police cruisers arrive with flashing lights.",
                "prev_scene_connection": "Final tactical heist escape resolution.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    "police_chase": {
        "id": "police_chase",
        "group": "Action & Adventure",
        "name": "High-Speed Police Cruiser Pursuit & PIT Evasion",
        "default_category": "Action & Adventure",
        "allowed_categories": ["Stories & Lore", "Cars & Comparisons"],
        "title": "Vice City Pursuit: Police AI Tactics, Spike Strip Roadblocks & PIT Evasion",
        "description": "Heart-pounding police chase through Vice City: aggressive squad car boxing formations, roadblock spike strips, helicopter searchlights, tactical PIT maneuver counter-steering, and high-speed highway evasion.",
        "banner": ("POLICE CHASE", "IN GTA 6 IS", "INSANE??"),
        "location": "Downtown Vice City to Biscayne Highway Overpass",
        "time_of_day": "Neon Night with Rain Slicked Streets",
        "weather": "Torrential tropical downpour with flashing red and blue siren reflections",
        "characters": "Lucia Caminos & Jason Duval",
        "vehicle": "Bravado Banshee GT (Pursuit Edition)",
        "central_event": "Four-Star High-Speed Police Pursuit & Tactical Roadblock Evasion",
        "narrative_arc": "Siren Alarm -> Squad Car Boxing -> Spike Strip Roadblock -> Tactical PIT Counter -> Helicopter Searchlight -> Tunnel Evasion Finale",
        "resolution": "Next-generation law enforcement AI in GTA 6 uses predictive flanking and tactical boxing to deliver heart-pounding pursuits.",
        "source": {
            "title": "IGN Factual Breakdown - GTA VI Police AI & Wanted System",
            "url": "https://www.ign.com/articles/gta-6-trailer-breakdown-details-you-missed",
            "source_name": "IGN Factual Breakdown",
            "reliability_score": 0.95,
            "published_at": "2023-12-06"
        },
        "claims": [
            ("Police AI coordinates multi-car boxing maneuvers and predictive roadblocks based on player heading.", 1, 0, "OFFICIAL"),
            ("Cruisers deploy spike strips dynamically across bottlenecks with tactical officer cover.", 1, 0, "VERIFIED_VISUAL"),
            ("Police helicopters utilize thermal searchlights that track vehicle engine heat through foliage.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Bravado Banshee roaring through neon streets with multiple police cruisers in close pursuit, red and blue lights reflecting off wet asphalt",
                "narration_text": "Police pursuits in Grand Theft Auto VI are completely redesigned with predictive flanking AI, aggressive PIT maneuvers, and coordinated roadblocks.",
                "subtitle_text": "Police pursuits in Grand Theft Auto VI are completely redesigned with predictive flanking AI, aggressive PIT maneuvers, and coordinated roadblocks.",
                "transition_type": "fade", "camera_movement": "Low-angle chase camera tracking inches behind vehicle with flashing siren glare",
                "action_progression": "Two patrol cruisers aggressively close in on the Banshee's rear bumper with sirens screaming.",
                "prev_scene_connection": "Opening visual hook establishing high-stakes pursuit.",
                "next_scene_connection": "Continuous high-speed sprint into multi-lane boulevard."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Police cruisers attempting to box in the Banshee from left and right lanes at 120 MPH",
                "narration_text": "Officers no longer mindlessly ram from behind. Squad cars coordinate in pairs, attempting to box your flanks and force your car onto curbs.",
                "subtitle_text": "Officers no longer mindlessly ram from behind. Squad cars coordinate in pairs, attempting to box your flanks and force your car onto curbs.",
                "transition_type": "cut", "camera_movement": "Dynamic side tracking shot showing flanking cruiser pushing against the driver door",
                "action_progression": "Jason counter-steers into the cruiser's quarter panel, breaking the boxing attempt.",
                "prev_scene_connection": "Continuation of pursuit into tactical contact.",
                "next_scene_connection": "Approaching an illuminated bridge roadblock."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Bridge roadblock with cruisers parked in V-formation and spike strips laid across the asphalt",
                "narration_text": "Ahead on the bridge, officers deploy tactical spike strips with cruisers parked in reinforced V-formations blocking primary lanes.",
                "subtitle_text": "Ahead on the bridge, officers deploy tactical spike strips with cruisers parked in reinforced V-formations blocking primary lanes.",
                "transition_type": "cut", "camera_movement": "Telephoto camera looking down the bridge framing the approaching roadblock",
                "action_progression": "Banshee swerves sharply through a narrow gap between the concrete barrier and parked cruiser.",
                "prev_scene_connection": "Direct progression from highway pursuit into the roadblock bottleneck.",
                "next_scene_connection": "Overhead spotlight blinding the windshield."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Police helicopter searchlight beaming directly down onto the speeding car cutting through heavy rain",
                "narration_text": "Air support brings heavy thermal spotlights that illuminate your vehicle through torrential rain, broadcasting your coordinates to ground units.",
                "subtitle_text": "Air support brings heavy thermal spotlights that illuminate your vehicle through torrential rain, broadcasting your coordinates to ground units.",
                "transition_type": "cut", "camera_movement": "High crane angle looking down through the piercing white beam of the helicopter spotlight",
                "action_progression": "Rotor wash whips rain across the pavement as the helicopter banks to track the car's heading.",
                "prev_scene_connection": "Continuation of escape under aerial pursuit.",
                "next_scene_connection": "Diving toward an underground tunnel entrance to break aerial line of sight."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Speeding into underground highway tunnel, breaking helicopter searchlight as sirens fade",
                "narration_text": "Diving into underground highway tunnels severs the helicopter's line of sight, creating a critical window to lose pursuit radar.",
                "subtitle_text": "Diving into underground highway tunnels severs the helicopter's line of sight, creating a critical window to lose pursuit radar.",
                "transition_type": "cut", "camera_movement": "Forward tracking camera rushing into illuminated tunnel mouth",
                "action_progression": "The searchlight cuts out as the vehicle plunges into the orange-lit tunnel corridor.",
                "prev_scene_connection": "Transition from open highway to underground evasion route.",
                "next_scene_connection": "Emerging on the quiet industrial access road."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Car idling in dark industrial warehouse alley as distant police sirens fade away into the rainy night",
                "narration_text": "What's your ultimate escape strategy when 5 stars hit? Outrun them or fight your way out? Let us know in the comments below!",
                "subtitle_text": "What's your ultimate escape strategy when 5 stars hit? Outrun them or fight your way out? Let us know in the comments below!",
                "transition_type": "fade", "camera_movement": "Slow cinematic crane pull-back as wanted stars begin flashing and disappear",
                "action_progression": "The vehicle idles in the dark alleyway as headlights click off and sirens fade in the distance.",
                "prev_scene_connection": "Final pursuit evasion and escape resolution.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    "crash_physics": {
        "id": "crash_physics",
        "group": "Vehicles & Transportation",
        "name": "Vehicle Crash Dynamics & Soft-Body Deformation",
        "default_category": "Cars & Comparisons",
        "allowed_categories": ["Cars & Comparisons", "Facts & Secrets"],
        "title": "GTA 6 Vehicle Crash Dynamics: Soft-Body Metal Deformation, Frame Twisting & Pole Impacts",
        "description": "Comprehensive technical breakdown of GTA 6's next-generation vehicle collision and soft-body deformation physics: concrete utility pole collisions, crumple zones, windshield spider-webbing, and post-crash recovery.",
        "banner": ("CRASH PHYSICS", "IN GTA 6 ARE", "MIND-BLOWING??"),
        "location": "Suburban Vice City Boulevard & Palm Avenue Intersection",
        "time_of_day": "Midday Sun with High-Contrast Road Glare",
        "weather": "Clear tropical afternoon with warm sunlight reflecting off car bodywork",
        "characters": "Jason Duval (Precision Driver)",
        "vehicle": "Pfister Comet S2 Sportscar (Impact Deformation Test)",
        "central_event": "High-Speed Pole Collision & Soft-Body Metal Deformation Analysis",
        "narrative_arc": "High-Speed Approach -> Loss of Traction -> Concrete Pole Collision -> Frame Deformation -> Radiator Steam -> Drift Recovery",
        "resolution": "Rockstar Games has engineered the most mathematically authentic vehicle destruction engine in open-world history.",
        "source": {
            "title": "Digital Foundry Technical Analysis - GTA VI Physics & Deformation Tech",
            "url": "https://www.digitalfoundry.net/articles/gta-6-damage-physics",
            "source_name": "Digital Foundry Tech Breakdown",
            "reliability_score": 0.95,
            "published_at": "2023-12-07"
        },
        "claims": [
            ("GTA 6 incorporates progressive soft-body metal deformation with volumetric panel crumpling.", 1, 0, "OFFICIAL"),
            ("Fixed roadside objects like concrete poles transfer realistic inertia, crushing front quarter panels.", 1, 0, "VERIFIED_VISUAL"),
            ("Windshields feature procedural safety-glass spider-webbing and detached bumper physics.", 1, 0, "VERIFIED_VISUAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Yellow Pfister Comet S2 speeding aggressively along suburban Vice City palm tree street",
                "narration_text": "Rockstar Games has completely rebuilt vehicle collision physics in Grand Theft Auto VI, introducing true multi-point soft-body metal deformation.",
                "subtitle_text": "Rockstar Games has completely rebuilt vehicle collision physics in Grand Theft Auto VI, introducing true multi-point soft-body metal deformation.",
                "transition_type": "fade", "camera_movement": "Low chase camera tracking the sportscar accelerating toward suburban intersection",
                "action_progression": "The Pfister Comet accelerates violently down the asphalt as tire squeal echoes past residential hedges.",
                "prev_scene_connection": "Opening visual hook establishing vehicle speed and handling.",
                "next_scene_connection": "Vehicle begins sudden aggressive oversteer heading toward the roadside curb."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Sportscar losing rear grip on tight corner apex, sliding sideways toward concrete utility pole",
                "narration_text": "Notice the weight transfer as the rear tires break traction. Independent suspension geometry compresses under extreme lateral G-forces.",
                "subtitle_text": "Notice the weight transfer as the rear tires break traction. Independent suspension geometry compresses under extreme lateral G-forces.",
                "transition_type": "cut", "camera_movement": "Mid-height tracking camera capturing counter-steer lock and tire smoke",
                "action_progression": "The rear end breaks loose into a heavy counter-steer slide heading dangerously close to the roadside pole.",
                "prev_scene_connection": "Direct progression from straight acceleration into loss of traction.",
                "next_scene_connection": "Front right quarter-panel impacting the concrete utility pole."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Front right fender violently impacting concrete utility pole with dynamic metal crumpling and shattered glass",
                "narration_text": "Impact! The front fender crumples with procedural accuracy. Rather than predefined dent morphs, the steel compresses around the solid concrete obstacle.",
                "subtitle_text": "Impact! The front fender crumples with procedural accuracy. Rather than predefined dent morphs, the steel compresses around the solid concrete obstacle.",
                "transition_type": "cut", "camera_movement": "Dynamic impact camera shaking violently with physics collision impulse",
                "action_progression": "The vehicle slams into the pole, violently shearing the front bumper and crushing the right fender.",
                "prev_scene_connection": "Direct continuation from the high-speed skid to the physical collision.",
                "next_scene_connection": "Car rebounding off the pole as radiator steam and debris billow."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Vehicle rebounding from pole with radiator steam venting and deformed hood panel buckled upward",
                "narration_text": "Watch the hood buckle upwards and the headlamp housing shatter. Internal engine components now have collision meshes that deform under structural load.",
                "subtitle_text": "Watch the hood buckle upwards and the headlamp housing shatter. Internal engine components now have collision meshes that deform under structural load.",
                "transition_type": "cut", "camera_movement": "Close rotational orbit inspecting the deformed right quarter panel and buckled hood",
                "action_progression": "Steam vents from the cracked radiator as the chassis settles back onto the pavement.",
                "prev_scene_connection": "Continuation of physics aftermath immediately following impact.",
                "next_scene_connection": "Driver engaging reverse gear and spinning the tires to disengage."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Damaged sportscar reversing away with asymmetrical steering wobble and scraping bumper",
                "narration_text": "Post-impact driving dynamics reflect the mechanical trauma: alignment pulling to the right, tire rubbing against crumpled wheel arches, and reduced top speed.",
                "subtitle_text": "Post-impact driving dynamics reflect the mechanical trauma: alignment pulling to the right, tire rubbing against crumpled wheel arches, and reduced top speed.",
                "transition_type": "cut", "camera_movement": "Low angle side camera following the deformed front wheel struggling to steer straight",
                "action_progression": "Jason reverses cleanly away from the curb and re-enters the roadway, steering against the damaged suspension.",
                "prev_scene_connection": "Transition from standstill impact inspection to active mechanical recovery.",
                "next_scene_connection": "Vehicle accelerating down the avenue into the distance."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Battle-damaged sportscar speeding away into the sunny Vice City horizon with damaged exhaust echoing",
                "narration_text": "Will GTA 6 have the best driving and damage physics of any game ever made? What crash tests do you want to see next? Drop your thoughts below!",
                "subtitle_text": "Will GTA 6 have the best driving and damage physics of any game ever made? What crash tests do you want to see next? Drop your thoughts below!",
                "transition_type": "fade", "camera_movement": "Rising crane sweep trailing the damaged sportscar heading into the sunset",
                "action_progression": "The Pfister disappears down the palm tree avenue as the scene concludes.",
                "prev_scene_connection": "Final cinematic driving resolution.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    },

    "street_fitness": {
        "id": "street_fitness",
        "group": "Lifestyle & Entertainment",
        "name": "Character Fitness, Stamina & Neighborhood Life",
        "default_category": "Stories & Lore",
        "allowed_categories": ["Stories & Lore", "Facts & Secrets"],
        "title": "Vice City Living World: Character Cardio Workouts, Muscle Fatigue & Street Encounters",
        "description": "Exploring GTA 6's living open world and character vitality systems: on-foot jogging through residential streets, dynamic cardio recovery, crouching vehicle inspections, and contextual neighborhood NPC encounters.",
        "banner": ("STREET LIVING WORLD", "IN GTA 6 IS", "UNMATCHED??"),
        "location": "Little Haiti Residential Enclave & Suburban Parking District",
        "time_of_day": "Warm Afternoon Sunlight with Long Palm Shadows",
        "weather": "Sunny Florida afternoon with gentle breeze rustling palm fronds",
        "characters": "Jason Duval (Athletic Attire)",
        "vehicle": "None (On-Foot Pedestrian Jogging & Fitness)",
        "central_event": "Neighborhood On-Foot Exploration & Character Fitness Mechanics",
        "narrative_arc": "Residential Street Jog -> Cardio Workout Trigger -> Muscle Fatigue Recovery -> Parking Lot Vehicle Inspection -> Crouch Examination -> Sunset Walk",
        "resolution": "From physical cardio stamina systems to living neighborhood AI, GTA 6 brings unprecedented depth to every pedestrian moment.",
        "source": {
            "title": "IGN Gameplay Analysis - GTA VI Living World & Character Systems",
            "url": "https://www.ign.com/articles/gta-6-character-mechanics-breakdown",
            "source_name": "IGN Gameplay Breakdown",
            "reliability_score": 0.95,
            "published_at": "2023-12-06"
        },
        "claims": [
            ("GTA 6 features dynamic character fitness and cardio stamina meters that deplete and regenerate realistically.", 1, 0, "VERIFIED_VISUAL"),
            ("Characters physically react to heavy exertion with panting animations and temporary muscle recovery delays.", 1, 0, "VERIFIED_VISUAL"),
            ("Residential neighborhoods feature interactive pedestrian encounters, parked exotic cars, and contextual inspections.", 1, 0, "OFFICIAL")
        ],
        "scenes": [
            {
                "scene_number": 1, "start_time": 0.0, "end_time": 8.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Jason jogging smoothly along a sunlit Vice City neighborhood sidewalk lined with lush palm trees",
                "narration_text": "Grand Theft Auto VI is bringing back comprehensive character physical conditioning, introducing dynamic cardio workouts, muscle stamina, and true living neighborhoods.",
                "subtitle_text": "Grand Theft Auto VI is bringing back comprehensive character physical conditioning, introducing dynamic cardio workouts, muscle stamina, and true living neighborhoods.",
                "transition_type": "fade", "camera_movement": "Mid-height steadycam tracking smoothly alongside Jason jogging down the sidewalk",
                "action_progression": "Jason maintains a steady jogging cadence as afternoon sunlight filters through swaying palm fronds.",
                "prev_scene_connection": "Opening visual hook establishing on-foot character motion and neighborhood atmosphere.",
                "next_scene_connection": "Camera follows Jason as physical exertion triggers the on-screen stamina notification."
            },
            {
                "scene_number": 2, "start_time": 8.5, "end_time": 17.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Cardio Workout stamina notification appearing on screen as Jason slows to catch his breath",
                "narration_text": "Sustained running directly engages the character's cardio system. The HUD alerts you to rest and recover, with realistic breathing audio and visible chest heave.",
                "subtitle_text": "Sustained running directly engages the character's cardio system. The HUD alerts you to rest and recover, with realistic breathing audio and visible chest heave.",
                "transition_type": "cut", "camera_movement": "Over-the-shoulder tracking shot showing the dynamic stamina gauge and exhaustion animations",
                "action_progression": "Jason slows his pace to a brisk walk as the stamina meter begins gradual recovery.",
                "prev_scene_connection": "Direct progression from active sprint to cardio recovery.",
                "next_scene_connection": "Turning into a sunlit residential parking courtyard with parked luxury vehicles."
            },
            {
                "scene_number": 3, "start_time": 17.5, "end_time": 26.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Jason walking into a quiet residential parking lot with high-end luxury SUVs parked in the sun",
                "narration_text": "Every neighborhood in Vice City has its own economic tier. Here in this quiet enclave, multi-million dollar SUVs and exotic sports coupes sit parked in open driveways.",
                "subtitle_text": "Every neighborhood in Vice City has its own economic tier. Here in this quiet enclave, multi-million dollar SUVs and exotic sports coupes sit parked in open driveways.",
                "transition_type": "cut", "camera_movement": "Wide cinematic tracking shot gliding past parked vehicles and tropical landscaping",
                "action_progression": "Jason scans the parked vehicles as he walks across the warm asphalt toward an exotic red SUV.",
                "prev_scene_connection": "Transition from residential street into parking courtyard.",
                "next_scene_connection": "Jason approaching the vehicle to inspect it closely."
            },
            {
                "scene_number": 4, "start_time": 26.5, "end_time": 35.5,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Jason crouching down beside a luxury red SUV to inspect its forged alloy wheels and brake calipers",
                "narration_text": "Contextual inspection animations let you crouch down and study intricate details: custom carbon-ceramic brake discs, tread wear, and unique wheel configurations.",
                "subtitle_text": "Contextual inspection animations let you crouch down and study intricate details: custom carbon-ceramic brake discs, tread wear, and unique wheel configurations.",
                "transition_type": "cut", "camera_movement": "Low-angle close-up rotating smoothly around Jason crouching beside the vehicle wheel",
                "action_progression": "Jason crouches low, examining the intricate gold-finished multi-spoke wheel design.",
                "prev_scene_connection": "Direct continuation from walking up to the vehicle to crouching in inspection.",
                "next_scene_connection": "Standing back up and looking down the quiet neighborhood street."
            },
            {
                "scene_number": 5, "start_time": 35.5, "end_time": 44.5,
                "visual_type": "ORIGINAL_SIMULATION", "is_fictional": 1,
                "visual_prompt": "Standing up as civilian neighbors converse on nearby lawns and street traffic idles past",
                "narration_text": "NPCs react naturally to your presence. Linger too long near high-end property and homeowners look over suspiciously or notify local security patrols.",
                "subtitle_text": "NPCs react naturally to your presence. Linger too long near high-end property and homeowners look over suspiciously or notify local security patrols.",
                "transition_type": "cut", "camera_movement": "Smooth crane rise looking out over the peaceful suburban neighborhood skyline",
                "action_progression": "Jason stands upright, stretches his shoulders, and continues walking down the quiet sidewalk.",
                "prev_scene_connection": "Transition from vehicle inspection back to open-world pedestrian traversal.",
                "next_scene_connection": "Walking into the golden sunset at the end of the avenue."
            },
            {
                "scene_number": 6, "start_time": 44.5, "end_time": 53.0,
                "visual_type": "3D_GAMEPLAY_FOOTAGE", "is_fictional": 0,
                "visual_prompt": "Jason walking toward the sunset horizon as evening shadows lengthen across the neighborhood",
                "narration_text": "Are you spending time exploring every corner of Vice City on foot? What neighborhood secrets are you hunting first? Tell us in the comments below!",
                "subtitle_text": "Are you spending time exploring every corner of Vice City on foot? What neighborhood secrets are you hunting first? Tell us in the comments below!",
                "transition_type": "fade", "camera_movement": "Cinematic pull-back crane shot framing Jason walking into the warm golden twilight",
                "action_progression": "The sun dips below the palm tree canopy as nocturnal insects begin chirping in the warm breeze.",
                "prev_scene_connection": "Final peaceful lifestyle and narrative resolution.",
                "next_scene_connection": "Fade to outro."
            }
        ]
    }
}

def get_all_activities() -> dict:
    """Returns the full registry of GTA 6 activities."""
    return ACTIVITY_REGISTRY

def get_activity_by_id(activity_id: str) -> dict:
    """Retrieves an activity blueprint by its identifier."""
    return ACTIVITY_REGISTRY.get(activity_id)

def get_recent_activity_history(limit: int = 50) -> list:
    """
    Queries SQLite database to extract history of previously generated and exported topics,
    activities, locations, and narrative arcs to strictly prevent repetitive content.
    """
    conn = get_connection()
    cur = conn.cursor()
    history = []
    try:
        # First gather all officially exported videos across all dates
        cur.execute("""
            SELECT s.category, s.title, sb.story_title, sb.environment_location,
                   sb.vehicle, sb.central_event, sb.narrative_arc, t.activity_type, p.created_at,
                   1 as is_exported
            FROM exported_videos ev
            JOIN video_projects p ON ev.project_id = p.id
            JOIN scripts s ON p.script_id = s.id
            LEFT JOIN storyboards sb ON p.id = sb.project_id
            LEFT JOIN topics t ON s.topic_id = t.id
            ORDER BY ev.id DESC
        """)
        for r in cur.fetchall():
            history.append(dict(r))

        # Also gather recent project history
        cur.execute("""
            SELECT s.category, s.title, sb.story_title, sb.environment_location,
                   sb.vehicle, sb.central_event, sb.narrative_arc, t.activity_type, p.created_at,
                   0 as is_exported
            FROM video_projects p
            JOIN scripts s ON p.script_id = s.id
            LEFT JOIN storyboards sb ON p.id = sb.project_id
            LEFT JOIN topics t ON s.topic_id = t.id
            ORDER BY p.created_at DESC LIMIT ?
        """, (limit,))
        for r in cur.fetchall():
            history.append(dict(r))
    except Exception:
        pass
    finally:
        conn.close()
    return history

def select_intelligent_daily_activities(preferred_activity_ids: list = None) -> list:
    """
    Autonomously selects exactly 3 diverse, unrepeated activities across the 4 activity groups:
    - Walking & Exploration
    - Vehicles & Transportation
    - Lifestyle & Entertainment
    - Action & Crime Scenarios
    Completely decoupled from the rigid 3-category taxonomy in compliance with
    GTA6_SCENE_VARIETY_DIRECTIVE.md.
    """
    if preferred_activity_ids:
        mapped_items = []
        for f_id in preferred_activity_ids:
            act = get_activity_by_id(f_id)
            if act:
                mapped_items.append({
                    "category": act["group"],
                    "activity": act
                })
        if len(mapped_items) == 3:
            return mapped_items

    history = get_recent_activity_history(50)
    used_activity_ids = []
    for h in history:
        act_type = h.get("activity_type")
        if act_type and act_type in ACTIVITY_REGISTRY and act_type not in used_activity_ids:
            used_activity_ids.append(act_type)

    # Group all blueprints by the 4 scene groups
    group_mapping = {
        "Walking & Exploration": "Walking & Exploration",
        "Vehicles & Transportation": "Vehicles & Transportation",
        "Vehicles & Transportation / Aviation": "Vehicles & Transportation",
        "Lifestyle & Entertainment": "Lifestyle & Entertainment",
        "Action & Crime Scenarios": "Action & Crime Scenarios",
        "Action & Adventure": "Action & Crime Scenarios"
    }
    groups = {
        "Walking & Exploration": [],
        "Vehicles & Transportation": [],
        "Lifestyle & Entertainment": [],
        "Action & Crime Scenarios": []
    }
    for act in ACTIVITY_REGISTRY.values():
        grp = group_mapping.get(act.get("group", ""), "Walking & Exploration")
        if grp in groups:
            groups[grp].append(act)

    # Check group usage history to prioritize groups that have not been used recently
    recent_group_usage = []
    for h in history:
        act_id = h.get("activity_type")
        act = ACTIVITY_REGISTRY.get(act_id)
        if act:
            g = group_mapping.get(act.get("group", ""), "")
            if g and g not in recent_group_usage:
                recent_group_usage.append(g)

    def score_candidate(cand):
        c_id = cand["id"]
        if c_id not in used_activity_ids:
            return 10000.0
        pos = used_activity_ids.index(c_id)
        return -1000.0 + (pos * 10.0)

    for g in groups:
        groups[g].sort(key=score_candidate, reverse=True)

    # Rank the 4 scene groups by novelty / rotation recency so all 4 groups rotate evenly
    import random
    group_scores = []
    for gname, cand_list in groups.items():
        if cand_list:
            top_cand = cand_list[0]
            cand_score = score_candidate(top_cand)
            # Group recency bonus: Groups not in recent history get +20000 bonus
            if gname not in recent_group_usage:
                group_bonus = 20000.0 + random.uniform(5.0, 15.0)
            else:
                group_bonus = (recent_group_usage.index(gname) * 50.0) + random.uniform(1.0, 5.0)
            total_score = cand_score + group_bonus
            group_scores.append((total_score, gname, top_cand))

    group_scores.sort(key=lambda x: x[0], reverse=True)

    selected = []
    for _, gname, top_cand in group_scores[:3]:
        selected.append({
            "category": gname,
            "activity": top_cand
        })

    return selected
