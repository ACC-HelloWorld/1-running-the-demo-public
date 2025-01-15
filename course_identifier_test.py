from course_identifier import course_id, HIVEMQ_USERNAME, HIVEMQ_PASSWORD, HIVEMQ_HOST

from uuid import uuid4  # universally unique identifier
from self_driving_lab_demo import (
    SelfDrivingLabDemoLight,
    mqtt_observe_sensor_data,
    get_paho_client,
)


def test_course_identifier():
    """Check that a demo with the course ID as PICO_ID runs without errors"""

    # Your course ID will act like a "codeword" to identify your data
    PICO_ID = course_id
    assert PICO_ID is not "test"
    dummy = False
    log_to_database = False
    SESSION_ID = str(uuid4())
    print(f"session ID: {SESSION_ID}")

    # instantiate client once and reuse (to avoid opening too many connections)
    client = get_paho_client(
        f"sdl-demo/picow/{PICO_ID}/as7341/",
        username=HIVEMQ_USERNAME,
        password=HIVEMQ_PASSWORD,
        hostname=HIVEMQ_HOST,
    )

    sdl = SelfDrivingLabDemoLight(
        autoload=True,  # perform target data experiment automatically
        simulation=dummy,  # run simulation instead of physical experiment
        observe_sensor_data_fn=mqtt_observe_sensor_data,  # (default)
        observe_sensor_data_kwargs=dict(
            pico_id=PICO_ID,
            session_id=SESSION_ID,
            client=client,
            mongodb=log_to_database,
        ),
    )
    results = sdl.evaluate(dict(R=10, G=11, B=12))
    print(results)
