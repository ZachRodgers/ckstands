import json
from pathlib import Path

pngs = [
    "armour_stand_wand.png","grab.png","left_leg_rotation_selected.png","right_arm_rotation.png","step_sideways.png",
    "arms.png","grad_selected.png","lock.png","right_arm_rotation_selected.png","step_sideways_selected.png",
    "arms_selected.png","gravity.png","lock_selected.png","right_hand_item.png","step_spin.png",
    "base_plate.png","gravity_selected.png","name_tag_visibility.png","right_leg_rotation.png","step_spin_selected.png",
    "base_plate_selected.png","head_rotation.png","name_tag_visibility_selected.png","right_leg_rotation_selected.png","step_y.png",
    "body_rotation.png","head_rotation_selected.png","orientation.png","scale.png","step_y_selected.png",
    "body_rotation_selected.png","help.png","orientation_selected.png","scale_selected.png","visibility.png",
    "copy_paste.png","left_arm_rotation.png","position.png","size.png","visibility_selected.png",
    "copy_paste_selected.png","left_arm_rotation_selected.png","position_selected.png","size_selected.png",
    "equipmented_selected.png","left_hand_item.png","reset.png","step_forwards.png",
    "equipment.png","left_leg_rotation.png","reset_selected.png","step_forwards_selected.png"
]

out_dir = Path(".")
template_parent = "minecraft:item/generated"
template_ns = "minecraft:custom"

for png in pngs:
    base = Path(png).stem
    data = {
        "parent": template_parent,
        "textures": {
            "layer0": f"{template_ns}/{base}"
        }
    }
    out_path = out_dir / f"{base}.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
