using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShipTwo : MonoBehaviour
{
    public Transform otherShip; // The other ship's position, angle, and speed
    public Rigidbody rb;
    public float speed = 50.0f;
    public float alphaAngle = 30.0f;
    public float betaDistance = 10.0f;
    public Rigidbody otherShipRB;
    [Range(0.0f, 10.0f)]
    public float aggressionLevel = 7.0f;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();

        // Maintain constant velocity in forward direction
        rb.velocity = new Vector3(0, 0, speed);
        Random.InitState(43);
        StartCoroutine("Movements");
    }

    // Update is called once per frame
    void Update()
    {

    }

    // Use this function for physics within Unity
    private void FixedUpdate()
    {
        Vector3 targetDir = otherShip.position - transform.position;
        float angle = Vector3.Angle(targetDir, transform.forward);

        float distance = Mathf.Abs(Vector3.Distance(otherShip.position, transform.position));

        float errorTolerance = 5.0f;



        if (angle < alphaAngle + errorTolerance && angle > alphaAngle - errorTolerance)
        {
            if (distance < betaDistance + errorTolerance && distance > betaDistance - errorTolerance)
            {
                Debug.Log("Destroyed Ship One!");
            }
        }
        //Debug.Log("Angle == " + angle);
        //if (angle < 5.0f)
        //    print("close");

        
        //StartCoroutine("EscapeAwayFrom", 4.5f);
        //StartCoroutine("GoToward", 4.5f);

        // Adjust velocity to always aim from front of ship
        rb.velocity = transform.forward * speed;
    }

    IEnumerator Movements()
    {
        while (true)
        {
            yield return new WaitForSeconds(Random.Range(1, 3));
            if (Random.Range(0, 10) > aggressionLevel)
            {
                //Debug.Log("Ship Two: Escaping away from");
                EscapeAwayFrom(0.0f);
            }
            else
            {
                //Debug.Log("Ship Two: Going toward");
                GoToward(0.0f);
            }
        }
        
    }
    public void EscapeAwayFrom(float timeToWait)
    {
        float timeForPredictedPath = 50.0f;

        // Get predicted path of other ship 5 seconds from now
        Vector3 expectedOtherShipPosition = otherShipRB.position + otherShipRB.velocity * timeForPredictedPath * Time.deltaTime;

        // ROTATE AWAY FROM CODE
        // Determine which direction to rotate towarsds
        Vector3 targetDirection = transform.position - expectedOtherShipPosition;

        // The step size is equal to speed times frame time.
        float singleStep = speed * Time.deltaTime;

        // Rotate the forward vector towards the target direction by one step
        Vector3 newDirection = Vector3.RotateTowards(transform.forward, targetDirection, singleStep, 0.0f);

        // Draw a ray pointing at our target in
        Debug.DrawRay(transform.position, expectedOtherShipPosition - transform.position, Color.red);//, 1.0f);

        // Calculate a rotation a step closer to the target and applies rotation to this object
        transform.rotation = Quaternion.LookRotation(newDirection);

        // END ROTATE AWAY FROM CODE
    }

    public void GoToward(float timeToWait)
    {
        float timeForPredictedPath = 50.0f;

        // Get predicted path of other ship 5 seconds from now
        Vector3 expectedOtherShipPosition = otherShipRB.position + otherShipRB.velocity * timeForPredictedPath * Time.deltaTime;

        // ROTATE TOWARD CODE
        // Determine which direction to rotate towards
        Vector3 targetDirection = expectedOtherShipPosition - transform.position;

        // The step size is equal to speed times frame time.
        float singleStep = speed * Time.deltaTime;

        // Rotate the forward vector towards the target direction by one step
        Vector3 newDirection = Vector3.RotateTowards(transform.forward, targetDirection, singleStep, 0.0f);

        // Draw a ray pointing at our target in
        Debug.DrawRay(transform.position, expectedOtherShipPosition - transform.position, Color.red);//, 1.0f);

        // Calculate a rotation a step closer to the target and applies rotation to this object
        transform.rotation = Quaternion.LookRotation(newDirection);


        // END ROTATE TOWARD CODE
    }
}


//using System.Collections;
//using System.Collections.Generic;
//using UnityEngine;

//public class Escaper : MonoBehaviour
//{
//    // Get position of chaser to escape from
//    public Transform otherShip;
//    public Rigidbody rb;
//    public float speed = 50.0f;
//    // Start is called before the first frame update
//    void Start()
//    {
//        rb = GetComponent<Rigidbody>();

//        // Maintain constant velocity in forward direction
//        rb.velocity = new Vector3(0, 0, speed);
//    }

//    // Update is called once per frame
//    void Update()
//    {

//    }

//    private void FixedUpdate()
//    {
//        // Go at 90 angle away from chaser
//        //transform.Translate()

//        // Get chaser's angle
//        Vector3 chaserAngles = otherShip.rotation.eulerAngles;
//        Debug.Log("ChaserAngle = " + chaserAngles.ToString());
//        Debug.Log("Escaper Angle = " + transform.eulerAngles.ToString());

//        // Change Escaper's angle to be opposite of Chaser's angle
//        //float x = transform.rotation.eulerAngles.y;
//        transform.eulerAngles = new Vector3(chaserAngles.x + 180, chaserAngles.y + 180, transform.eulerAngles.z + 180);

//        //transform.Rotate()
//    }
//}
