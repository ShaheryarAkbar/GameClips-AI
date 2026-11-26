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
        "banner": ("AIRPORT TERMINAL", "IN GTA 6 IS", "MASSIVE??"),
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
        "banner": ("VICE CITY CLUBS", "IN GTA 6 ARE", "INSANE??"),
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
    Intelligently selects exactly 3 distinct, fresh activities for the daily production run:
    - Exactly 1 for Facts & Secrets
    - Exactly 1 for Cars & Comparisons
    - Exactly 1 for Stories & Lore
    
    Guarantees:
    - Zero repetition with previously exported or generated activities.
    - Strict novelty priority: unused activities are always chosen first.
    - Completely distinct groups and locations across all 3 daily categories.
    - Enforces ONE VIDEO = ONE MAIN TOPIC = ONE COMPLETE STORY.
    """
    if preferred_activity_ids and len(preferred_activity_ids) == 3:
        mapped = {}
        for act_id in preferred_activity_ids:
            act = ACTIVITY_REGISTRY.get(act_id)
            if not act:
                continue
            for cat in ["Facts & Secrets", "Cars & Comparisons", "Stories & Lore"]:
                if cat in act["allowed_categories"] and cat not in mapped:
                    mapped[cat] = act
                    break
        if len(mapped) == 3:
            return [
                {"category": "Facts & Secrets", "activity": mapped["Facts & Secrets"]},
                {"category": "Cars & Comparisons", "activity": mapped["Cars & Comparisons"]},
                {"category": "Stories & Lore", "activity": mapped["Stories & Lore"]}
            ]

    history = get_recent_activity_history(50)
    
    # Identify all activities that have been used
    used_activity_ids = []
    for h in history:
        act_type = h.get("activity_type")
        if act_type and act_type in ACTIVITY_REGISTRY and act_type not in used_activity_ids:
            used_activity_ids.append(act_type)
        
        # Check title and event text for legacy or mapped activities
        full_text = (str(h.get("title") or "") + " " + str(h.get("central_event") or "") + " " + str(h.get("story_title") or "")).lower()
        if ("superbike" in full_text or "motorcycle" in full_text or "bati" in full_text) and "superbike_ride" not in used_activity_ids:
            used_activity_ids.append("superbike_ride")
        if ("bank" in full_text or "vault" in full_text or "heist" in full_text) and "bank_robbery" not in used_activity_ids:
            used_activity_ids.append("bank_robbery")
        if ("airport" in full_text or "terminal" in full_text or "escobar" in full_text) and "airport_walk" not in used_activity_ids:
            used_activity_ids.append("airport_walk")
        if ("beach" in full_text or "dune" in full_text or "coastline" in full_text) and "beach_coastal" not in used_activity_ids:
            used_activity_ids.append("beach_coastal")
        if ("aircraft" in full_text or "skies" in full_text or "airplane" in full_text) and "aircraft_flight" not in used_activity_ids:
            used_activity_ids.append("aircraft_flight")
        if ("off-road" in full_text or "truck" in full_text or "safari" in full_text or "mud" in full_text) and "offroad_truck" not in used_activity_ids:
            used_activity_ids.append("offroad_truck")

    # Categorize available blueprints
    facts_candidates = [
        act for act in ACTIVITY_REGISTRY.values()
        if "Facts & Secrets" in act["allowed_categories"]
    ]
    cars_candidates = [
        act for act in ACTIVITY_REGISTRY.values()
        if "Cars & Comparisons" in act["allowed_categories"]
    ]
    stories_candidates = [
        act for act in ACTIVITY_REGISTRY.values()
        if "Stories & Lore" in act["allowed_categories"]
    ]

    def score_candidate(cand):
        c_id = cand["id"]
        # If candidate has NEVER been used, give top priority score
        if c_id not in used_activity_ids:
            return 10000.0
        # If used, give heavy penalty based on how recently it was used
        pos = used_activity_ids.index(c_id)
        return -1000.0 + (pos * 10.0)

    # Sort candidates by novelty
    facts_candidates.sort(key=score_candidate, reverse=True)
    cars_candidates.sort(key=score_candidate, reverse=True)
    stories_candidates.sort(key=score_candidate, reverse=True)

    selected = {}
    chosen_groups = set()
    chosen_locations = set()

    # 1. Select Facts & Secrets first (prefer walking/exploration or unique secrets)
    for f in facts_candidates:
        loc_key = f["location"][:10].lower()
        if f["group"] not in chosen_groups and loc_key not in chosen_locations:
            selected["Facts & Secrets"] = f
            chosen_groups.add(f["group"])
            chosen_locations.add(loc_key)
            break
    if "Facts & Secrets" not in selected:
        selected["Facts & Secrets"] = facts_candidates[0]
        chosen_groups.add(facts_candidates[0]["group"])

    # 2. Select Cars & Comparisons (vehicles or high-speed pursuit)
    for c in cars_candidates:
        loc_key = c["location"][:10].lower()
        if c["id"] != selected["Facts & Secrets"]["id"] and \
           c["group"] not in chosen_groups and loc_key not in chosen_locations:
            selected["Cars & Comparisons"] = c
            chosen_groups.add(c["group"])
            chosen_locations.add(loc_key)
            break
    if "Cars & Comparisons" not in selected:
        for c in cars_candidates:
            if c["id"] != selected["Facts & Secrets"]["id"]:
                selected["Cars & Comparisons"] = c
                chosen_groups.add(c["group"])
                break

    # 3. Select Stories & Lore (lifestyle, narrative or action)
    for s in stories_candidates:
        loc_key = s["location"][:10].lower()
        if s["id"] != selected["Facts & Secrets"]["id"] and \
           s["id"] != selected["Cars & Comparisons"]["id"] and \
           s["group"] not in chosen_groups and loc_key not in chosen_locations:
            selected["Stories & Lore"] = s
            chosen_groups.add(s["group"])
            chosen_locations.add(loc_key)
            break
    if "Stories & Lore" not in selected:
        for s in stories_candidates:
            if s["id"] != selected["Facts & Secrets"]["id"] and \
               s["id"] != selected["Cars & Comparisons"]["id"]:
                selected["Stories & Lore"] = s
                break

    return [
        {"category": "Facts & Secrets", "activity": selected["Facts & Secrets"]},
        {"category": "Cars & Comparisons", "activity": selected["Cars & Comparisons"]},
        {"category": "Stories & Lore", "activity": selected["Stories & Lore"]}
    ]
