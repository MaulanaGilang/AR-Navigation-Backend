# Correctly parsing the complete JSON data
json_data = [
    {
        "id": 9,
        "places1_id": 8,
        "places2_id": 34,
        "distance": 0.111318308761353,
        "status": True
    },
    {
        "id": 22,
        "places1_id": 33,
        "places2_id": 108,
        "distance": 0.039344340737687,
        "status": True
    },
    {
        "id": 11,
        "places1_id": 9,
        "places2_id": 49,
        "distance": 0.084679089452983,
        "status": True
    },
    {
        "id": 13,
        "places1_id": 15,
        "places2_id": 44,
        "distance": 0.451726906241127,
        "status": True
    },
    {
        "id": 8,
        "places1_id": 7,
        "places2_id": 112,
        "distance": 0.165661664544771,
        "status": True
    },
    {
        "id": 15,
        "places1_id": 26,
        "places2_id": 51,
        "distance": 0.045024352510404,
        "status": True
    },
    {
        "id": 17,
        "places1_id": 29,
        "places2_id": 45,
        "distance": 0.080452068295891,
        "status": True
    },
    {
        "id": 18,
        "places1_id": 30,
        "places2_id": 46,
        "distance": 0.012524443263008,
        "status": True
    },
    {
        "id": 19,
        "places1_id": 31,
        "places2_id": 47,
        "distance": 0.057489992959592,
        "status": True
    },
    {
        "id": 61,
        "places1_id": 106,
        "places2_id": 34,
        "distance": 0.031402307177642,
        "status": True
    },
    {
        "id": 20,
        "places1_id": 32,
        "places2_id": 53,
        "distance": 0.13741493872112,
        "status": True
    },
    {
        "id": 21,
        "places1_id": 33,
        "places2_id": 8,
        "distance": 0.199842769421455,
        "status": True
    },
    {
        "id": 65,
        "places1_id": 108,
        "places2_id": 113,
        "distance": 0.015686542197598,
        "status": True
    },
    {
        "id": 24,
        "places1_id": 35,
        "places2_id": 32,
        "distance": 0.050934229801426,
        "status": True
    },
    {
        "id": 25,
        "places1_id": 35,
        "places2_id": 3,
        "distance": 0.04397049634975,
        "status": True
    },
    {
        "id": 26,
        "places1_id": 36,
        "places2_id": 2,
        "distance": 0.058716291539785,
        "status": True
    },
    {
        "id": 27,
        "places1_id": 36,
        "places2_id": 35,
        "distance": 0.031364665586072,
        "status": True
    },
    {
        "id": 28,
        "places1_id": 36,
        "places2_id": 52,
        "distance": 0.046232686057444,
        "status": True
    },
    {
        "id": 29,
        "places1_id": 37,
        "places2_id": 26,
        "distance": 0.083706407001668,
        "status": True
    },
    {
        "id": 30,
        "places1_id": 37,
        "places2_id": 36,
        "distance": 0.060954670186617,
        "status": True
    },
    {
        "id": 31,
        "places1_id": 38,
        "places2_id": 7,
        "distance": 0.073144300797542,
        "status": True
    },
    {
        "id": 32,
        "places1_id": 38,
        "places2_id": 29,
        "distance": 0.067079703666656,
        "status": True
    },
    {
        "id": 33,
        "places1_id": 39,
        "places2_id": 37,
        "distance": 0.070499620257123,
        "status": True
    },
    {
        "id": 34,
        "places1_id": 39,
        "places2_id": 40,
        "distance": 0.062264615810463,
        "status": True
    },
    {
        "id": 38,
        "places1_id": 42,
        "places2_id": 9,
        "distance": 0.03692741041529,
        "status": True
    },
    {
        "id": 39,
        "places1_id": 42,
        "places2_id": 43,
        "distance": 0.041035787479653,
        "status": True
    },
    {
        "id": 40,
        "places1_id": 43,
        "places2_id": 44,
        "distance": 0.0478789771685,
        "status": True
    },
    {
        "id": 41,
        "places1_id": 45,
        "places2_id": 30,
        "distance": 0.051946239158648,
        "status": True
    },
    {
        "id": 42,
        "places1_id": 46,
        "places2_id": 47,
        "distance": 0.058870831735414,
        "status": True
    },
    {
        "id": 44,
        "places1_id": 49,
        "places2_id": 15,
        "distance": 0.413158257862259,
        "status": True
    },
    {
        "id": 45,
        "places1_id": 49,
        "places2_id": 10,
        "distance": 0.096075857539124,
        "status": True
    },
    {
        "id": 66,
        "places1_id": 109,
        "places2_id": 110,
        "distance": 0.089347197506967,
        "status": True
    },
    {
        "id": 67,
        "places1_id": 110,
        "places2_id": 111,
        "distance": 0.111349171184387,
        "status": True
    },
    {
        "id": 47,
        "places1_id": 52,
        "places2_id": 32,
        "distance": 0.038933915979106,
        "status": True
    },
    {
        "id": 3,
        "places1_id": 5,
        "places2_id": 101,
        "distance": 0.027263709469293,
        "status": True
    },
    {
        "id": 4,
        "places1_id": 6,
        "places2_id": 101,
        "distance": 0.020929874620312,
        "status": True
    },
    {
        "id": 5,
        "places1_id": 101,
        "places2_id": 37,
        "distance": 0.051805755283054,
        "status": True
    },
    {
        "id": 70,
        "places1_id": 111,
        "places2_id": 112,
        "distance": 0.008676009146204,
        "status": True
    },
    {
        "id": 53,
        "places1_id": 39,
        "places2_id": 112,
        "distance": 0.019954202426803,
        "status": True
    },
    {
        "id": 62,
        "places1_id": 106,
        "places2_id": 108,
        "distance": 0.038310005763607,
        "status": True
    },
    {
        "id": 69,
        "places1_id": 109,
        "places2_id": 113,
        "distance": 0.022258203073377,
        "status": True
    },
    {
        "id": 52,
        "places1_id": 27,
        "places2_id": 101,
        "distance": 0.039755126479401,
        "status": True
    },
    {
        "id": 10,
        "places1_id": 9,
        "places2_id": 104,
        "distance": 0.050558136960457,
        "status": True
    },
    {
        "id": 23,
        "places1_id": 34,
        "places2_id": 103,
        "distance": 0.027965984845383,
        "status": True
    },
    {
        "id": 54,
        "places1_id": 102,
        "places2_id": 103,
        "distance": 0.022466628975443,
        "status": True
    },
    {
        "id": 55,
        "places1_id": 102,
        "places2_id": 104,
        "distance": 0.035254642959672,
        "status": True
    },
    {
        "id": 56,
        "places1_id": 103,
        "places2_id": 105,
        "distance": 0.033259912573584,
        "status": True
    },
    {
        "id": 2,
        "places1_id": 114,
        "places2_id": 40,
        "distance": 0.071948289474016,
        "status": True
    },
    {
        "id": 37,
        "places1_id": 41,
        "places2_id": 114,
        "distance": 0.061345794488741,
        "status": True
    },
    {
        "id": 46,
        "places1_id": 14,
        "places2_id": 116,
        "distance": 0.045822339812048,
        "status": True
    },
    {
        "id": 71,
        "places1_id": 114,
        "places2_id": 4,
        "distance": 0.015822999326864,
        "status": True
    },
    {
        "id": 72,
        "places1_id": 116,
        "places2_id": 115,
        "distance": 22957748433995,
        "status": True
    },
    {
        "id": 73,
        "places1_id": 115,
        "places2_id": 40,
        "distance": 0.013406258503854,
        "status": True
    },
    {
        "id": 57,
        "places1_id": 104,
        "places2_id": 105,
        "distance": 0.020666664141912,
        "status": True
    },
    {
        "id": 58,
        "places1_id": 104,
        "places2_id": 41,
        "distance": 0.023103199583371,
        "status": True
    },
    {
        "id": 59,
        "places1_id": 105,
        "places2_id": 106,
        "distance": 0.027414733619153,
        "status": True
    },
    {
        "id": 60,
        "places1_id": 105,
        "places2_id": 107,
        "distance": 0.035938705038229,
        "status": True
    },
    {
        "id": 49,
        "places1_id": 54,
        "places2_id": 55,
        "distance": 1,
        "status": True
    },
    {
        "id": 50,
        "places1_id": 56,
        "places2_id": 54,
        "distance": 1,
        "status": True
    },
    {
        "id": 51,
        "places1_id": 57,
        "places2_id": 56,
        "distance": 1,
        "status": True
    },
    {
        "id": 16,
        "places1_id": 27,
        "places2_id": 38,
        "distance": 0.06211742500786,
        "status": True
    },
    {
        "id": 1,
        "places1_id": 1,
        "places2_id": 33,
        "distance": 0.050488817470318,
        "status": True
    },
    {
        "id": 6,
        "places1_id": 6,
        "places2_id": 28,
        "distance": 0.068625958916436,
        "status": True
    },
    {
        "id": 7,
        "places1_id": 7,
        "places2_id": 1,
        "distance": 0.034146421992735,
        "status": True
    },
    {
        "id": 63,
        "places1_id": 107,
        "places2_id": 108,
        "distance": 0.026004086433193,
        "status": True
    },
    {
        "id": 64,
        "places1_id": 107,
        "places2_id": 41,
        "distance": 0.029662725197522,
        "status": True
    },
    {
        "id": 68,
        "places1_id": 102,
        "places2_id": 42,
        "distance": 0.009351125829221,
        "status": True
    }
]

# Generate Mermaid graph notation
mermaid_graph = "graph LR\n"
for entry in json_data:
    mermaid_graph += f"    {entry['places1_id']} -- \"{entry['distance']}\" --> {entry['places2_id']}\n"

# Display the generated graph notation
mermaid_graph_trimmed = "\n".join(mermaid_graph.split("\n")[:69]) 
print(mermaid_graph_trimmed)

