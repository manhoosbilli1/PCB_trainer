import pcbnew

# Load the board
board = pcbnew.GetBoard()

# Function to add via to each pad in the footprint
def add_vias_to_footprint(footprint, via_diameter, drill_diameter):
    for pad in footprint.Pads():
        # Create a new via
        via = pcbnew.VIA(board)
        via.SetDrill(drill_diameter)
        via.SetWidth(via_diameter)
        
        # Set via position to pad center
        via.SetPosition(pad.GetPosition())
        
        # Add via to board
        board.Add(via)

# Parameters
via_diameter = pcbnew.FromMM(0.2)  # 0.2mm
drill_diameter = pcbnew.FromMM(0.1)  # 0.1mm

# Iterate through all footprints and add vias to pads
for footprint in board.GetFootprints():
    add_vias_to_footprint(footprint, via_diameter, drill_diameter)

# Save the modified board
pcbnew.SaveBoard("/Users/shoaib/Projects/PCB_trainer/output_file.kicad_pcb", board)

