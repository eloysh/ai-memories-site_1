from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List


MASTER_STYLE = """
Ultra-premium prestige Russian TV drama.
Cold evening courtyard, warm headlights and streetlights, wet asphalt reflections,
realistic Russian apartment building exterior, expensive cinematic composition.
Restrained acting, micro-expressions only, no hysteria.
One single cinematic frame. Vertical 9:16. No text. No watermark.
""".strip()

NEGATIVE_BLOCK = """
Negative: no text, no watermark, no subtitles, no logo, no collage, no split screen,
no storyboard layout, no extra characters, no random cars, no changed faces,
no changed hairstyles, no changed outfits, no plastic skin, no beauty filter,
no cartoon style, no fantasy lighting, no horror, no blood, no overacting,
no screaming expression, no distorted hands, no distorted pregnancy belly,
no dark muddy underexposed image.
""".strip()

CHARACTER_BLOCKS = {
    "Kristina": """
Kristina: exact same Kristina from uploaded references. Beautiful blonde woman 28-32,
long soft wavy golden-blonde hair, blue eyes, delicate feminine features, fair realistic skin.
Late pregnancy, large natural baby bump clearly visible under a dark grey oversized knit dress.
Exhausted but unbreakable, emotionally restrained, no face drift, no redesign, no age change.
""".strip(),
    "Dima": """
Dima: exact same Dima from uploaded references. Dark-haired man 30-35, short styled dark hair,
light stubble, strong polished jawline, blue-gray cold eyes. Black slim turtleneck under dark coat.
Controlled, expensive, but emotionally breaking inside. No face drift, no redesign, not rugged, not older.
""".strip(),
    "Artyom": """
Artyom: exact same Artyom from uploaded references. Warm masculine face, short dark brown hair,
light stubble, calm protective presence. Dark olive jacket, white t-shirt, dark jeans, boots.
Soft reliable energy, not aggressive, no face drift, no redesign.
""".strip(),
    "Vasily": """
Vasily: exact same Vasily from uploaded references. Man 58-63, silver-gray styled hair,
calm intelligent face, dignified age lines. Black cashmere coat, dark turtleneck.
Quiet old Russian power, inevitable presence. No face drift, no redesign.
""".strip(),
    "Mother": """
Mother: exact same mother from uploaded references. Woman 50-55, light hair in loose bun,
worried blue eyes, fair skin, beige cardigan. Real maternal presence, tired and worried,
not theatrical, no face drift, no redesign.
""".strip(),
}


@dataclass
class Scene:
    id: str
    title: str
    scene_type: str
    timing: str
    characters: List[str]
    action: str
    camera: str
    dialogue: str = ""


def showrunner_agent(episode_title: str, story: str) -> List[Scene]:
    """Stable showrunner for S4E1. Later this can be replaced by an LLM call."""
    return [
        Scene(
            id="scene_01",
            title="Кристина выходит",
            scene_type="main",
            timing="0:04-0:13",
            characters=["Kristina"],
            action="Pregnant Kristina pushes open the heavy metal entrance door of a Soviet-era apartment building, steps into the night courtyard, stops, and automatically places one hand on her large pregnant belly.",
            camera="Low angle, slightly to her right, slow right-to-left drift feeling. Artyom's dark car is far in the blurred background.",
            dialogue="Artyom: Долго. Kristina: Зато вышла.",
        ),
        Scene(
            id="link_01_02",
            title="Объятие и reveal Димы",
            scene_type="transition",
            timing="0:13-0:23",
            characters=["Kristina", "Artyom", "Dima"],
            action="Kristina reaches Artyom near his car and leans into him for support, not romance. Her forehead rests on his shoulder. In the windshield reflection of a black luxury car, Dima's face is visible watching silently.",
            camera="Camera moves slowly around them right-to-left until Dima's reflection becomes stronger than the embrace.",
        ),
        Scene(
            id="scene_02",
            title="Дима в машине",
            scene_type="main",
            timing="0:23-0:32",
            characters=["Dima"],
            action="Dima sits inside the black luxury car. Extreme close-up of his hand gripping the steering wheel, then his eyes through the windshield. His control cracks silently.",
            camera="Cold dashboard light, windshield reflections, slow right-to-left drift feeling.",
        ),
        Scene(
            id="link_02_03",
            title="Дима выходит и идёт",
            scene_type="transition",
            timing="0:32-0:42",
            characters=["Dima", "Kristina", "Artyom"],
            action="Dima steps out of the car, closes the door calmly, and walks across the wet courtyard toward Kristina and Artyom. He does not hurry.",
            camera="Behind-the-shoulder tracking shot, low angle, right-to-left movement.",
        ),
        Scene(
            id="link_03_04",
            title="Артём видит Диму",
            scene_type="transition",
            timing="0:42-0:50",
            characters=["Artyom", "Kristina", "Dima"],
            action="Artyom sees Dima approaching. His arm around Kristina stays. He turns slightly toward Dima, calm and alert, positioning himself beside Kristina, not in front of her.",
            camera="Medium shot, restrained acting, cold evening light.",
            dialogue="Kristina: Он здесь? Artyom: Да. Kristina: Не уходи. Artyom: Никуда.",
        ),
        Scene(
            id="scene_03",
            title="Столкновение",
            scene_type="main",
            timing="0:50-1:02",
            characters=["Dima", "Artyom", "Kristina"],
            action="Dima stops two meters from Artyom. They face each other. Kristina stands beside Artyom, visible and present, not hidden behind him.",
            camera="Wide enough to hold all three. Wet courtyard between the men. Visible breath in cold air.",
            dialogue="Dima: Уйди. Artyom: Нет. Dima: Это не твоё. Artyom: Она сама решает — чьё.",
        ),
        Scene(
            id="link_04_punch",
            title="Полсекунды перед ударом",
            scene_type="transition",
            timing="1:02-1:08",
            characters=["Dima"],
            action="Extreme close-up of Dima's face after Artyom's painful line. The words land. His eyes drop for a fraction of a second, shoulder drops, weight shifts forward. Control breaks.",
            camera="Extreme close-up, no cinematic heroism, ugly human restraint breaking.",
        ),
        Scene(
            id="scene_04",
            title="Удар и драка",
            scene_type="main",
            timing="1:08-1:20",
            characters=["Dima", "Artyom"],
            action="A short realistic fight near the car. The punch lands or is partially deflected. Dima's coat is grabbed. Artyom is pushed against the car. Both breathe hard. Neither is winning.",
            camera="Slight handheld instability only here. No blood, no slow motion, no choreography.",
        ),
        Scene(
            id="link_04_05",
            title="Кристина между ними",
            scene_type="transition",
            timing="1:20-1:28",
            characters=["Kristina", "Dima", "Artyom"],
            action="Pregnant Kristina steps into the space between Dima and Artyom. Both men freeze. Her pregnancy is not weakness here; it is authority.",
            camera="Camera stabilizes again. Kristina centered, men on both sides.",
            dialogue="Kristina: Стоп. Оба. Стоп.",
        ),
        Scene(
            id="scene_05",
            title="Схватка",
            scene_type="main",
            timing="1:28-1:36",
            characters=["Kristina"],
            action="A sudden contraction hits Kristina. Her eyes close sharply, one hand grips her belly, the other reaches for the car for support. She bends slightly at the waist and breathes through it.",
            camera="Medium close-up focused fully on her physical pain and restraint.",
            dialogue="Kristina: Подождите…",
        ),
        Scene(
            id="link_05_mother",
            title="Мама слышна до кадра",
            scene_type="transition",
            timing="1:36-1:43",
            characters=["Kristina", "Mother", "Dima", "Artyom"],
            action="Kristina breathes through the contraction. Artyom moves carefully toward her. Running footsteps come from the building entrance before Mother appears. Mother bursts out and runs to Kristina.",
            camera="Camera follows the sound toward the entrance, then back to Kristina.",
            dialogue="Mother: Ты с ума сошёл? Dima: Не лезь. Mother: Она моя дочь.",
        ),
        Scene(
            id="scene_06",
            title="Дима тянется — она отходит",
            scene_type="main",
            timing="1:43-1:51",
            characters=["Dima", "Kristina"],
            action="Dima's control is gone. Not anger, something rawer. His hand lifts slightly toward Kristina, not grabbing, just reaching. Kristina sees the hand and takes one small step back. His hand drops.",
            camera="Close emotional composition, silence, right-to-left drift.",
        ),
        Scene(
            id="link_06_vasily",
            title="Фары Василия",
            scene_type="transition",
            timing="1:51-1:58",
            characters=["Dima", "Artyom", "Kristina", "Mother"],
            action="Wide shot of all four in the courtyard. Headlights sweep across the wet asphalt from the gate. All four turn toward the light simultaneously. The black Mercedes stops.",
            camera="Wide shot, light as pressure, engine sound then silence.",
        ),
        Scene(
            id="scene_07",
            title="Василий прибывает",
            scene_type="main",
            timing="1:58-2:10",
            characters=["Vasily", "Dima", "Kristina"],
            action="Vasily steps out of the black Mercedes, closes the door calmly, reads the courtyard, finds Kristina with his eyes and walks toward her. He passes within one meter of Dima and does not look at him.",
            camera="Low angle tracking, slow right-to-left, inevitable power.",
            dialogue="Vasily: Кристина. Поехали.",
        ),
        Scene(
            id="link_07_choice",
            title="Выбор",
            scene_type="transition",
            timing="2:10-2:22",
            characters=["Kristina", "Dima", "Artyom", "Vasily"],
            action="Kristina stands in the center. Vasily holds the open Mercedes door. Artyom watches quietly. Dima is further away. She looks at Dima, then at Artyom, then at Vasily and the open door.",
            camera="Triangle composition, Kristina centered, three looks.",
            dialogue="Dima: Не садись к нему. Kristina: Поздно.",
        ),
        Scene(
            id="link_goodbye_artyom",
            title="Прощание с Артёмом",
            scene_type="transition",
            timing="2:22-2:28",
            characters=["Kristina", "Artyom", "Vasily"],
            action="Before getting into the Mercedes, Kristina looks at Artyom. He touches her hand for one second, then lets go and steps back. His face says: go, I am here.",
            camera="Intimate restrained medium close-up, open car door nearby.",
            dialogue="Artyom: Я здесь буду. Kristina: Знаю.",
        ),
        Scene(
            id="scene_08_final",
            title="Финал — Дима один",
            scene_type="main",
            timing="2:28-2:42",
            characters=["Dima", "Artyom", "Mother"],
            action="The Mercedes leaves. Red taillights stretch over the wet asphalt. Dima stands alone in the foreground, motionless, coat slightly dishevelled. Artyom watches in the middle ground. Mother cries silently near the building.",
            camera="Wide shot. Camera becomes completely still. Only the car moves. Dima looks empty, like a man who lost.",
        ),
    ]


def continuity_agent(scene: Scene) -> str:
    blocks = [CHARACTER_BLOCKS[name] for name in scene.characters if name in CHARACTER_BLOCKS]
    return "\n\n".join(blocks)


def nano_prompt_agent(scene: Scene) -> str:
    return f"""
Use the uploaded references as strict identity and continuity sources.

{MASTER_STYLE}

{continuity_agent(scene)}

SCENE: {scene.title}
TYPE: {scene.scene_type}
TIMING: {scene.timing}

ACTION:
{scene.action}

CAMERA AND COMPOSITION:
{scene.camera}

QUALITY RULES:
Keep exact identity, outfit, age, hair, proportions, pregnancy, cars and courtyard continuity.
Make faces visible and clean, not muddy. The frame must be bright enough to read emotion.
One single cinematic frame only.

{NEGATIVE_BLOCK}
""".strip()


def grok_prompt_agent(scene: Scene) -> str:
    return f"""
Use the approved generated frame as the strict reference.
Keep exact identity, hair, outfit, lighting, background, proportions and camera angle.
No face drift. No redesign. No overacting. No cartoon motion. No text. No watermark.

SCENE: {scene.title}
ACTION: {scene.action}

ANIMATION PLAN:
Beat 1: Hold the emotional tension. Minimal movement. Natural breathing.
Beat 2: Add tiny eye movement, restrained body reaction, and realistic micro-expression.
Beat 3: End on a strong quiet emotional frame that can cut into the next scene.

CAMERA:
Slow right-to-left cinematic drift, except fight scene may have slight instability.

DIALOGUE / SOUND REFERENCE:
{scene.dialogue or "Silence, breath, wet asphalt, distant city."}

Duration: 10 seconds. Aspect ratio: 9:16. Resolution: 720p.
""".strip()


def post_agent(episode_title: str) -> Dict[str, Any]:
    return {
        "caption": "Он думал, что всё ещё контролирует.\n\nПока не увидел, как она смотрит на другого.\n\nВышел из машины.\nСорвался.\nПотерял.\n\nОна сказала одно слово.\n\n«Поздно»\n\nИ уехала.\n\nА он остался стоять в пустом дворе.\n\nВпервые в жизни — просто стоять.\n\nЭто и есть Сезон 4.",
        "pinned_comment": "Один вопрос:\n\nДима потерял её — или сам себя?\n\n1 — её\n2 — себя\n3 — и то и другое\n\n👇",
        "hashtags": ["#золотаяклетка", "#сезон4", "#нейросериал", "#aiсериал", "#reels"],
        "cover_options": [
            "ТЫ ЕЁ ПОТЕРЯЛ / сезон 4 • серия 1",
            "ПОЗДНО / и это всё что она сказала",
            "ОН СТОЯЛ И СМОТРЕЛ / КАК ОНА УЕЗЖАЕТ",
        ],
    }


def create_episode_pack(episode_title: str, story: str) -> Dict[str, Any]:
    scenes = showrunner_agent(episode_title, story)
    return {
        "episode_title": episode_title,
        "story": story,
        "rules": {
            "aspect_ratio": "9:16",
            "camera": "slow right-to-left drift",
            "light": "cold evening + warm headlights",
            "rhythm": "slow, restrained, premium drama",
        },
        "scenes": [
            {
                **asdict(scene),
                "nano_prompt": nano_prompt_agent(scene),
                "grok_prompt": grok_prompt_agent(scene),
            }
            for scene in scenes
        ],
        "post_pack": post_agent(episode_title),
    }
